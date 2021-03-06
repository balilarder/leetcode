from typing import List

import pytest

from .solutions import ListNode, Solution


def create_node(reverse_num_list: List[int]):
    first_node = ListNode(reverse_num_list[0])
    test_node = first_node
    for num in reverse_num_list[1:]:
        test_node.next = ListNode(num)
        test_node = test_node.next
    return first_node


def assert_node_value_equal(node_1, node_2):
    while node_1 is not None and node_2 is not None:
        if node_1.val != node_2.val:
            return False

        node_1 = node_1.next
        node_2 = node_2.next

    if node_1 is not None or node_2 is not None:
        return False

    return True


@pytest.mark.parametrize(
    "test_node1_val,test_node2_val,expected_val",
    [([2, 4, 3], [5, 6, 4], [7, 0, 8]), ([0], [7, 3], [7, 3]), ([5], [5], [0, 1])],
)
def test_solution(test_node1_val, test_node2_val, expected_val):
    test_node1 = create_node(test_node1_val)
    test_node2 = create_node(test_node2_val)
    expected_node = create_node(expected_val)

    solution = Solution()
    result_node = solution.addTwoNumbers(test_node1, test_node2)
    assert assert_node_value_equal(result_node, expected_node)
