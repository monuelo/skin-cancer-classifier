# Skin Cancer Classifier
Skin cancer classification demo with Federated Learning


## About
This is a demo around training a skin cancer classification model with PyGrid


#### What is Federated Learning?
_"It's a simple, powerful way to train Deep Learning models. If you think about training data, it's always the result of some sort of collection process. People (via devices) generate data by recording events in the real world. Normally, this data is aggregated to a single, central location so that you can train a machine learning model. Federated Learning turns this on its head!_

_Instead of bringing training data to the model (a central server), you bring the model to the training data (wherever it may live)._

_The idea is that this allows whoever is creating the data to own the only permanent copy, and thus maintain control over who ever has access to it. Pretty cool, eh?"_ 

Text by **Andrew Trask** - Twitter: [@iamtrask](twitter.com/iamtrask)

### Tools

#### PyGrid

PyGrid is a peer-to-peer network of data owners and data scientists who can collectively train AI models using [PySyft](https://github.com/OpenMined/PySyft/).

Repository: https://github.com/OpenMined/PyGrid


#### PySyft

PySyft is a Python library for secure and private Deep Learning. PySyft decouples private data from model training, using Federated Learning, Differential Privacy, and Multi-Party Computation (MPC) within the main Deep Learning frameworks like PyTorch and TensorFlow.

Repository: https://github.com/OpenMined/PySyft
