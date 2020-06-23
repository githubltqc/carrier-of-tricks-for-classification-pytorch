import argparse

def get_args():
    parser = argparse.ArgumentParser()

    # model architecture & checkpoint
    parser.add_argument('--model', type=str, default='ResNet50')
    parser.add_argument('--norm', type=str, default='batchnorm')
    parser.add_argument('--num_classes', type=int, default=6)
    parser.add_argument('--pretrained', type=bool, default=True)
    parser.add_argument('--pretrained_path', type=str, default=None)
    parser.add_argument('--checkpoint_dir', type=str, default='checkpoint')
    parser.add_argument('--checkpoint_name', type=str, default='')
    parser.add_argument('--zero_gamma', type=bool, default=False)

    # data loading
    parser.add_argument('--num_workers', type=int, default=0)
    parser.add_argument('--seed', type=int, default=42, help='random seed')

    # training hyper parameters
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--epochs', type=int, default=120)
    parser.add_argument('--log_interval', type=int, default=20)
    parser.add_argument('--evaluate', action='store_true', default=False)

    # optimzier & learning rate scheduler
    parser.add_argument('--learning_rate', type=float, default=0.1)
    parser.add_argument('--weight_decay', type=float, default=0.0001)
    parser.add_argument('--optimizer', default='SGD', choices=('SGD', 'ADAM'),
                        help='optimizer to use (SGD | ADAM)')
    parser.add_argument('--decay_type', default='step', choices=('step', 'step_warmup', 'cosine_warmup'),
                        help='optimizer to use (step | step_warmup | cosine_warmup)')

    args = parser.parse_args()
    return args
