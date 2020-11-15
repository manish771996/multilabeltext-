import argparse


def parameter_parser():
    """
    A method to parse up command line parameters.
    The default hyperparameters give good results without cross-validation.
    """
    parser = argparse.ArgumentParser(description="Run HARNN.")

    # Data Parameters
    parser.add_argument("--train-file",
                        nargs="?",
                        default="../data/Train_sample.json",
                        help="Training data.")

    parser.add_argument("--validation-file",
                        nargs="?",
                        default="../data/Validation_sample.json",
                        help="Validation data.")

    parser.add_argument("--test-file",
                        nargs="?",
                        default="../data/Test_sample.json",
                        help="Testing data.")

    parser.add_argument("--metadata-file",
                        nargs="?",
                        default="../data/metadata.tsv",
                        help="Metadata file for embedding visualization.")

    parser.add_argument("--word2vec-file",
                        nargs="?",
                        default="../data/word2vec_100.kv",
                        help="Word2vec file for embedding characters (the dim need to be the same as embedding dim).")

    # Model Hyperparameters
    parser.add_argument("--pad-seq-len",
                        type=int,
                        default=150,
                        help="Padding sequence length of data. (depends on the data)")

    parser.add_argument("--embedding-type",
                        type=int,
                        default=1,
                        help="The embedding type. (default: 1)")

    parser.add_argument("--embedding-dim",
                        type=int,
                        default=100,
                        help="Dimensionality of character embedding. (default: 100)")

    parser.add_argument("--lstm-dim",
                        type=int,
                        default=256,
                        help="Dimensionality of LSTM neurons. (default: 256)")

    parser.add_argument("--lstm-layers",
                        type=int,
                        default=1,
                        help="Number of LSTM layers. (default: 1)")

    parser.add_argument("--attention-dim",
                        type=int,
                        default=200,
                        help="Dimensionality of Attention neurons. (default: 200)")

    parser.add_argument("--attention-penalization",
                        type=bool,
                        default=True,
                        help="Use attention penalization or not. (default: True)")

    parser.add_argument("--fc-dim",
                        type=int,
                        default=512,
                        help="Dimensionality for FC neurons. (default: 512)")

    parser.add_argument("--dropout-rate",
                        type=float,
                        default=0.5,
                        help="Dropout keep probability. (default: 0.5)")

    parser.add_argument("--alpha",
                        type=float,
                        default=0.5,
                        help="Weight of global part in scores cal. (default: 0.5)")

    parser.add_argument("--num-classes-list",
                        type=list,
                        default=[9, 128, 661, 8364],
                        help="Each number of labels in hierarchical structure. (depends on the task)")

    parser.add_argument("--total-classes",
                        type=int,
                        default=9162,
                        help="Total number of labels. (depends on the task)")

    parser.add_argument("--topK",
                        type=int,
                        default=5,
                        help="Number of top K prediction classes. (default: 5)")

    parser.add_argument("--threshold",
                        type=float,
                        default=0.5,
                        help="Threshold for prediction classes. (default: 0.5)")

    # Training Parameters
    parser.add_argument("--epochs",
                        type=int,
                        default=20,
                        help="Number of training epochs. (default: 20)")

    parser.add_argument("--batch-size",
                        type=int,
                        default=32,
                        help="Batch Size. (default: 32)")

    parser.add_argument("--learning-rate",
                        type=float,
                        default=0.001,
                        help="Learning rate. (default: 0.001)")

    parser.add_argument("--decay-rate",
                        type=float,
                        default=0.95,
                        help="Rate of decay for learning rate. (default: 0.95)")

    parser.add_argument("--decay-steps",
                        type=int,
                        default=500,
                        help="How many steps before decay learning rate. (default: 500)")

    parser.add_argument("--evaluate-steps",
                        type=int,
                        default=10,
                        help="Evaluate model on val set after how many steps. (default: 50)")

    parser.add_argument("--norm-ratio",
                        type=float,
                        default=1.25,
                        help="The ratio of the sum of gradients norms of trainable variable. (default: 1.25)")

    parser.add_argument("--l2-lambda",
                        type=float,
                        default=0.0,
                        help="L2 regularization lambda. (default: 0.0)")

    parser.add_argument("--checkpoint-steps",
                        type=int,
                        default=10,
                        help="Save model after how many steps. (default: 50)")

    parser.add_argument("--num-checkpoints",
                        type=int,
                        default=10,
                        help="Number of checkpoints to store. (default: 10)")

    # Misc Parameters
    parser.add_argument("--allow-soft-placement",
                        type=bool,
                        default=True,
                        help="Allow device soft device placement. (default: True)")

    parser.add_argument("--log-device-placement",
                        type=bool,
                        default=False,
                        help="Log placement of ops on devices. (default: False)")

    parser.add_argument("--gpu-options-allow-growth",
                        type=bool,
                        default=True,
                        help="Allow gpu options growth. (default: True)")

    return parser.parse_args()