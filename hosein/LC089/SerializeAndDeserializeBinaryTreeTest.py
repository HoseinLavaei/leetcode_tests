from .SerializeAndDeserializeBinaryTree import Codec
from .SerializeAndDeserializeBinaryTree import TreeNode

def test_serialize_and_deserialize_binary_tree():
    input_string = "1,2,,,3,4,,,5,,"
    tree = Codec().deserialize(input_string)
    output_string = Codec().serialize(tree)
    assert input_string == output_string