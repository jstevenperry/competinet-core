#
# The various activation functions that can be added to a layer

from enum import Enum

from domain.base_model import BaseModel


class Activation(Enum, BaseModel):
    """
    Activations. These are the ones currently supported by Keras.
    """
    RELU = 10
    SIGMOID = 20
    SOFTMAX = 30
    SOFTPLUS = 40
    SOFTSIGN = 50
    TANH = 60
    SELU = 70
    ELU = 80
    EXPONENTIAL = 90

