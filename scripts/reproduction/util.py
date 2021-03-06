# -*- coding: utf-8 -*-
__author__ = 'masayuki'

import numpy
import theano

def numpy_dataset(data_xy):
    '''
    dataset を numpy.ndarray として返す
    :param data_xy:
    :return:
    '''
    data_x, data_y = data_xy
    numpy_x = (
        data_x if isinstance(data_x, numpy.ndarray)
        else numpy.asarray(data_x, dtype=theano.config.floatX)
    )
    numpy_y = (
        data_y if isinstance(data_y, numpy.ndarray)
        else numpy.asarray(data_y, dtype=theano.config.floatX)
    )
    return (numpy_x, numpy_y)

def shared_dataset(data_xy, borrow=True):
    '''
    dataset を theano.shared として返す
    :param data_xy:
    :param borrow:
    :return:
    '''
    data_x, data_y = data_xy
    shared_x = (
        data_x if isinstance(data_x, theano.tensor.sharedvar.TensorSharedVariable)
        else (
            theano.shared(data_x, borrow=borrow) if isinstance(data_x, numpy.ndarray)
            else theano.shared(numpy.asarray(data_x, dtype=theano.config.floatX), borrow=borrow)
        )
    )
    shared_y = (
        data_y if isinstance(data_y, theano.tensor.sharedvar.TensorSharedVariable)
        else (
            theano.shared(data_y, borrow=borrow) if isinstance(data_y, numpy.ndarray)
            else theano.shared(numpy.asarray(data_y, dtype=theano.config.floatX), borrow=borrow)
        )
    )
    return (shared_x, shared_y)

def calculate_error_indexes(y, y_pred):
    '''
    MAE と MRE を返す
    :param y:
    :param y_pred:
    :return:
    '''
    # retrieve numpy ndarray

    print y

    mae = numpy.mean(numpy.abs(y - y_pred))
    mre = numpy.abs(y - y_pred / y)
    mre[mre == numpy.inf] = 0
    mre = numpy.mean(mre)
    rmse = numpy.sqrt(numpy.mean((y - y_pred) ** 2))

    return (mae, mre, rmse)