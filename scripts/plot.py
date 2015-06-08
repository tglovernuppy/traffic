import numpy
import matplotlib.pyplot as plt

def plot(Y, pred_Y=None, title='', block=True):
	''' Plot the actual Y and predicted Y

    :param Y: n-by-m actual data
    :param pred_Y: n-by-m predicted data
	'''
	# count the data
	n = len(Y)		# the number of observations
	m = len(Y[0])	# the number of observation locations
	# m=min(2,m)

	# create a Figure instance
	fig = plt.figure()

	# create axes
	ax = []
	for i in xrange(m):
		ax.append(fig.add_subplot(m,1,i+1))

	# plot the data
	Yt = Y.transpose()
	if pred_Y == None:
		for i in xrange(m):
			ax[i].plot(numpy.array(xrange(n)), Yt[i], "r.-")
	else:
		pred_Yt = pred_Y.transpose()
		for i in xrange(m):
			ax[i].plot(numpy.array(xrange(n)), Yt[i], "r.-")
			ax[i].plot(numpy.array(xrange(n)), pred_Yt[i], "b.-")

	plt.title(title)
	plt.show(block=block)
