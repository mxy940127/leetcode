# <p align="center">框架思维</p>



## 一、数据结构存储方式

**数据结构存储方式只有两种：数组（顺序存储）、链表（链式存储**



## 二、数据结构基本操作

**一言以蔽之：遍历+访问**     线性：for/while迭代 			非线性：递归

数组遍历框架

```python
def traverse(array: List[int]):
    for index in range(len(array)):
        // 迭代访问array[index]
```

链表遍历框架

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
def traverse(head: Optional[ListNode]):
    // 递归访问
    traverse(head.next)
    
def traverse(head: Optional[ListNode]):
    // 迭代访问
    while(head):
        // 操作head.val
        head = head.next
```

二叉树遍历框架

```python
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

// 非线性递归遍历
def traverse(root: Optional[TreeNode]):
    traverse(root.left)
    traverse(root.right)
```

N叉树遍历框架

```python
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
def traverse(root: Optional[Node]):
    for child in root.children:
        traverse(child)
```



## 三、刷题指南

1.先搞定数组、链表这类基本数据结构的常用算法，如单链表翻转、前缀和数组、二分搜索

2.**二叉树**一定要理解

```python
def traverse(root: Optional[TreeNode]):
    // 前序位置
    traverse(root.left);
    // 中序位置
    traverse(root.right);
    // 后序位置
```

3.动归、贪心等