from typing import List
import grpc
import numpy as np

from .grpc import x_client_pb2, x_client_pb2_grpc
from .grpc.utils import numpy_to_array, array_to_numpy


class XClient:
    def __init__(self, url, batch_size=16):
        channel_opt = [('grpc.max_send_message_length', 2 ** 31 - 1),
                       ('grpc.max_receive_message_length', 2 ** 31 - 1)]

        channel = grpc.insecure_channel(url, options=channel_opt)
        self._stub = x_client_pb2_grpc.XInferenceServerStub(channel)
        self.batch_size = batch_size

    def infer(self, images: List[np.ndarray]):
        def generate_request():
            batch_ids = list(range(0, len(images), self.batch_size)) + [len(images)]
            request = x_client_pb2.Request()
            for i in range(len(batch_ids) - 1):
                request.ClearField('images')
                request.images.extend(
                    [numpy_to_array(img) for img in
                     images[batch_ids[i]:batch_ids[i + 1]]]
                )
                yield request

        response = self._stub.infer(generate_request())
        return [[array_to_numpy(box) for box in response.box], [array_to_numpy(pose) for pose in response.pose]]
