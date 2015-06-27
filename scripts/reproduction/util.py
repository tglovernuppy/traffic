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
        theano.shared(data_x, borrow=borrow) if isinstance(data_x, numpy.ndarray)
        else theano.shared(numpy.asarray(data_x, dtype=theano.config.floatX), borrow=borrow)
    )
    shared_y = (
        theano.shared(data_y, borrow=borrow) if isinstance(data_y, numpy.ndarray)
        else theano.shared(numpy.asarray(data_y, dtype=theano.config.floatX), borrow=borrow)
    )
    return (shared_x, shared_y)