# syntax=docker/dockerfile:1
FROM tensorflow/serving:2.8.0

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

RUN wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2017_11_17.tar.gz
RUN mkdir tmp-dir
RUN mkdir -p /models/object-detection/1
RUN tar xvfz ssd_mobilenet_v1_coco_2017_11_17.tar.gz -C tmp-dir
RUN mv tmp-dir/ssd_mobilenet_v1_coco_2017_11_17/saved_model/* /models/object-detection/1
RUN rm -rf tmp-dir ssd_mobilenet_v1_coco_2017_11_17.tar.gz

ENV MODEL_NAME=object-detection

ENTRYPOINT ["/usr/bin/tf_serving_entrypoint.sh"]