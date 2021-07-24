from simpletransformers.classification import ClassificationModel

model = ClassificationModel(
    "bert", "outputs", use_cuda=False
)