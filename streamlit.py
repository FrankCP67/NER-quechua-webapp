from simpletransformers.ner import NERModel,NERArgs

args = NERArgs()
args.num_train_epochs = 10
args.learning_rate = 1e-4
args.overwrite_output_dir =True
args.train_batch_size = 32
args.eval_batch_size = 32

label=['B-ORG', 'O', 'B-LOC', 'I-LOC', 'B-PER', 'I-PER', 'I-ORG']

model = NERModel('bert', "input/bert-base-uncased",labels=label,args =args,use_cuda=False)
