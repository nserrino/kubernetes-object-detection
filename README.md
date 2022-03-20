# kubernetes-object-detection

A demo app on Kubernetes to run the Tensorflow object detection API.

## Instructions

Create the server:
```
kubectl -f apply model-server/model-server.yaml
```

Forward the port:
```
kubectl port-forward service/model-server 8501:8501
```

Run some load:
```
cd model-client
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python client.py
```


