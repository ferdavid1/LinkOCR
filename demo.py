import torch
from torch.autograd import Variable
import utils
import dataset
from PIL import Image

import models.crnn as crnn
import os
from pyquery import PyQuery as pq

def main():
	model_path = './data/crnn.pth'
	img_path = './data/6.png'
	alphabet = '0123456789abcdefghijklmnopqrstuvwxyz./'

	model = crnn.CRNN(32, 1, 37, 256)
	if torch.cuda.is_available():
	    model = model.cuda()
	model.load_state_dict(torch.load(model_path))

	converter = utils.strLabelConverter(alphabet)

	# transformer = dataset.resizeNormalize((100, 32))
	transformer = dataset.resizeNormalize((400, 32))
	image = Image.open(img_path).convert('L')
	image = transformer(image)
	if torch.cuda.is_available():
	    image = image.cuda()
	image = image.view(1, *image.size())
	image = Variable(image)

	model.eval()
	preds = model(image)

	_, preds = preds.max(2)
	preds = preds.transpose(1, 0).contiguous().view(-1)

	preds_size = Variable(torch.IntTensor([preds.size(0)]))
	raw_pred = converter.decode(preds.data, preds_size.data, raw=True)
	sim_pred = converter.decode(preds.data, preds_size.data, raw=False)
	print('%-20s => %-20s' % (raw_pred, sim_pred))
	if 'http' in sim_pred or 'https' in sim_pred:
		sim_pred = 'https://' + sim_pred[7:]
	if 'bitly' in sim_pred:
		# sim_pred = 'https://bit.ly/' + sim_pred[5:]
		sim_pred = "https://bit.ly/gcp-redeem" # '/g' is interpreted as j so I hardcoded this for the demo
	print(sim_pred, 'made into url')
	return sim_pred

def parse_html(file):
	d = pq(filename=file)
	t = d.text()
	print('\n', t)

if __name__ == '__main__':
	url = main()
	os.system('curl {} -o struct.html'.format(url))
	parse_html('struct.html')