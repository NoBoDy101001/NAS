#!/usr/bin/python
# -*- coding: utf-8 -*-

import tensorflow as tf

in1 = tf.constant([1., 2.], name='in1')
in2 = tf.Variable(tf.random_normal([2]), name='in2')
out = tf.add(in1, in2, name='add')

writer = tf.summary.FileWriter('graphs/', tf.get_default_graph())
writer.close()
