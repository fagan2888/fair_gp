import sys
from train_models import train_feat_model
from feat_common_args import common_args
from FeatFair import FeatFair
import json

dataset = sys.argv[1]
dataset_name = dataset.split('/')[-1].split('.')[0]
attributes = sys.argv[2]
seed = int(sys.argv[3])
rdir = sys.argv[4]

est = FeatFair(
            **common_args,
            sel = 'fair_lexicase',
            surv = 'nsga2',
            random_state=seed,
            )

# set up Feat NSGA2 model
perf, hv = train_feat_model(est, 'feat_flex_nsga2', dataset, attributes, seed,
        rdir)

