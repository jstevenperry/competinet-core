#
# The description of a network, including a trained network,
# the desired state of a trained network (as in, "please model a network
# that looks like this"), and so forth.

from model.base_model import BaseModel


class NetworkDescriptor(BaseModel):
    """
    Represents a trained network if is_trained is True, otherwise
    represents the desired parameters of a network to be trained
    """
    __slots__ = [
        "network_id", "number_of_inputs", "number_of_outputs", "seasons_trained", "network_hidden_layout",
        "activation_function", "loss_function", "output_layer_loss_function", "weight_init_function",
        "updater_function", "normalizer_function", "activation_function", "dropout", "training_error",
        "network_training_threshold", "hidden_layer_algorithm", "number_of_hidden_layers",
        "number_of_training_epochs", "when_trained", "accuracy", "precision", "recall", "f1_score",
        "l2", "network_type"
    ]

    def __init__(self, network_id):
        self.network_id = network_id

    def is_trained(self):
        return self.when_trained is not None

