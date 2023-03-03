import numpy as np

from x_client.grpc.x_client_pb2 import NdArray


def array_to_numpy(array: NdArray):
    return np.frombuffer(array.data, dtype=np.dtype(array.dtype)).reshape(array.shape)


def numpy_to_array(array: np.ndarray):
    return NdArray(data=array.tobytes(), shape=array.shape, dtype=array.dtype.name)
