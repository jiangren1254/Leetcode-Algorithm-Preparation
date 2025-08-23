# 二叉树

## 知识点

### 二叉树遍历

**前序遍历**：**先访问根节点**，再前序遍历左子树，再前序遍历右子树
**中序遍历**：先中序遍历左子树，**再访问根节点**，再中序遍历右子树
**后序遍历**：先后序遍历左子树，再后序遍历右子树，**再访问根节点**

注意点

- 以根访问顺序决定是什么遍历
- 左子树都是优先右子树

#### 递归模板

- 递归实现二叉树遍历非常简单，不同顺序区别仅在于访问父结点顺序

```Python
def preorder_rec(root):
    if root is None:
        return
    visit(root)
    preorder_rec(root.left)
    preorder_rec(root.right)
    return

def inorder_rec(root):
    if root is None:
        return
    inorder_rec(root.left)
    visit(root)
    inorder_rec(root.right)
    return

def postorder_rec(root):
    if root is None:
        return
    postorder_rec(root.left)
    postorder_rec(root.right)
    visit(root)
    return
```

#### [前序非递归](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)

- 本质上是图的DFS的一个特例，因此可以用栈来实现

```Python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        preorder = []
        if root is None:
            return preorder
        
        s = [root]
        while len(s) > 0:
            node = s.pop()
            preorder.append(node.val)
            if node.right is not None:
                s.append(node.right)
            if node.left is not None:
                s.append(node.left)
        
        return preorder
```

#### [中序非递归](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

```Python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        s, inorder = [], []
        node = root
        while len(s) > 0 or node is not None:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                inorder.append(node.val)
                node = node.right
        return inorder
```

#### [后序非递归](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)

```Python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        s, postorder = [], []
        node, last_visit = root, None
        
        while len(s) > 0 or node is not None:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                peek = s[-1]
                if peek.right is not None and last_visit != peek.right:
                    node = peek.right
                else:
                    last_visit = s.pop()
                    postorder.append(last_visit.val)
        
        
        return postorder
```

注意点

- 核心就是：根节点必须在右节点弹出之后，再弹出

DFS 深度搜索-从下向上（分治法）

```Python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return []
        
        left_result = self.preorderTraversal(root.left)
        right_result = self.preorderTraversal(root.right)
        
        return [root.val] + left_result + right_result
```

注意点：

> DFS 深度搜索（从上到下） 和分治法区别：前者一般将最终结果通过指针参数传入，后者一般递归返回结果最后合并

#### [BFS 层次遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

```Python
"""
collections 是 Python 的 内置标准库模块，提供了几种比内置类型更高效或更高级的数据结构,eg：deque、Counter、defaultdict、OrderedDict、namedtuple
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        levels = []
        if root is None:
            return levels
        #  初始化双端队列 bfs, 只包含根节点 root
        bfs = collections.deque([root])
        
        while len(bfs) > 0:
            levels.append([])
            
            level_size = len(bfs)
            for _ in range(level_size):
                # popleft() 是 deque 提供的方法，用来从队列左边（也就是队头）取出一个元素。
                node = bfs.popleft()
                # levels[-1]是一个列表
                levels[-1].append(node.val)
                
                if node.left is not None:
                    bfs.append(node.left)
                if node.right is not None:
                    bfs.append(node.right)
        
        return levels
```

### 分治法应用

先分别处理局部，再合并结果

适用场景

- 快速排序
- 归并排序
- 二叉树相关问题

分治法模板

- 递归返回条件
- 分段处理
- 合并结果

## 常见题目示例

### [maximum-depth-of-binary-tree](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

> 给定一个二叉树，找出其最大深度。

- 我的思路

```python
这种适合使用分治法，最大深度嘛
每个树当做一个整体，计算自己的最大深度就好了
分治法YYDs
```



- 思路 1：分治法

```Python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

- 思路 2：层序遍历

```Python
class Solution:
    def maxDepth(self, root: TreeNode) -> List[List[int]]:
        
        depth = 0
        if root is None:
            return depth
        
        bfs = collections.deque([root])
        
        while len(bfs) > 0:
            depth += 1
            level_size = len(bfs)
            for _ in range(level_size):
                node = bfs.popleft()
                if node.left is not None:
                    bfs.append(node.left)
                if node.right is not None:
                    bfs.append(node.right)
        
        return depth
```

### [balanced-binary-tree](https://leetcode-cn.com/problems/balanced-binary-tree/)

> 给定一个二叉树，判断它是否是高度平衡的二叉树。

- 我的思路
  - 分治法YYDS
  - 分治法从下到上
  - 在如何得到左右两边的深度的时候卡住了
    - 我的思路，在求平衡的时候返也返回深度，就是有两个返回值，isbalanced, depth（未尝试，感觉会很复杂）
    - 模板做法，和我的一样，但是当前函数是只能返回一个布尔值，不能返回两个
    - 解决，在函数内在写一个函数就好了
    - 感觉这个算法有点缺陷，当树早就不平衡的时候，还是要判断完，不能提前结束

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(root):
            if root is None:
                return True, 0

            leftIsBalanced, leftDepth = depth(root.left)
            rightIsBalanced, rightDepth = depth(root.right)
            
            
            return leftIsBalanced and  rightIsBalanced and abs(leftDepth- rightDepth) < 2, 1+max(leftDepth,rightDepth)
        result,_ = depth(root)

        return result

        
```



- 思路 1：分治法，左边平衡 && 右边平衡 && 左右两边高度 <= 1，

```Python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
 
        def depth(root):
            
            if root is None:
                return 0, True
            # dl: 左边深度
            # bl: Balanced
            dl, bl = depth(root.left)
            dr, br = depth(root.right)
            
            return max(dl, dr) + 1, bl and br and abs(dl - dr) < 2
        
        _, out = depth(root)
        
        return out
```

- 思路 2：使用后序遍历(左->右->根)实现分治法的迭代版本

```Python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
		
        # 节点node 、平衡0，不平衡-1、
        s = [[TreeNode(), -1, -1]]
        node, last = root, None
        while len(s) > 1 or node is not None:
            if node is not None:
                s.append([node, -1, -1])
                node = node.left
                if node is None:
                    s[-1][1] = 0
            else:
                peek = s[-1][0]
                if peek.right is not None and last != peek.right:
                    node = peek.right
                else:
                    if peek.right is None:
                        s[-1][2] = 0
                    last, dl, dr = s.pop()
                    if abs(dl - dr) > 1:
                        return False
                    d = max(dl, dr) + 1
                    if s[-1][1] == -1:
                        s[-1][1] = d
                    else:
                        s[-1][2] = d
        
        return True
```

> 补充知识：
>
> ![image-20250804081557671](assets\image-20250804081557671-1754266560717-1-1754266562851-3.png)

### [binary-tree-maximum-path-sum](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)

> 给定一个**非空**二叉树，返回其最大路径和。

- 我的思路：
  - 做题没思路，但看下面的题解了，看了一遍，尝试使用分治法解决
  - 左子树的最大路径，不好理解
  - 右子树的最大路径，不好理解
  - 通过根结点的最大路径，好理解
  - 问题是，怎么统计的左子树最大路径，是不是根节点+左右子树中的最大值，感觉理解的不对，理解的对
  - 定义一个全局最大路径，存储最大路径
  - 这个题只让求出了最大路径和，不需要求出路径，不要被示例带偏了
  - 一个使用分治法的小窍门，从下往上看，先看叶子结点

- 思路：分治法。最大路径的可能情况：左子树的最大路径，右子树的最大路径，或通过根结点的最大路径。其中通过根结点的最大路径值等于以左子树根结点为端点的最大路径值加以右子树根结点为端点的最大路径值再加上根结点值，这里还要考虑有负值的情况即负值路径需要丢弃不取。

```Python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.maxPath = float('-inf')
        
        def largest_path_ends_at(node):
            if node is None:
                return float('-inf')
            
            e_l = largest_path_ends_at(node.left)
            e_r = largest_path_ends_at(node.right)
            
            self.maxPath = max(self.maxPath, node.val + max(0, e_l) + max(0, e_r), e_l, e_r)
            
            return node.val + max(e_l, e_r, 0)
        
        largest_path_ends_at(root)
        return self.maxPath
```

- **largest** → 最大的
- **path** → 路径
- **ends_at** → 结束在……

合起来就是：
 👉 **“以某个节点作为终点的最大路径和”**

也就是说，这个函数返回的是 **从某个节点往下走**，能走出的最大路径和（必须以这个node**节点结尾**）。

### [lowest-common-ancestor-of-a-binary-tree](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)

> 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

- 思路：分治法，有左子树的公共祖先或者有右子树的公共祖先，就返回子树的祖先，否则返回根节点

```Python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None
```

### BFS 层次应用

### [binary-tree-zigzag-level-order-traversal](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)

> 给定一个二叉树，返回其节点值的锯齿形层次遍历。Z 字形遍历

- 思路：在BFS迭代模板上改用双端队列控制输出顺序

```Python
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        levels = []
        if root is None:
            return levels
        
        s = collections.deque([root])

        start_from_left = True
        while len(s) > 0:
            levels.append([])
            level_size = len(s)
            
            if start_from_left:
                for _ in range(level_size):
                    node = s.popleft()
                    levels[-1].append(node.val)
                    if node.left is not None:
                        s.append(node.left)
                    if node.right is not None:
                        s.append(node.right)
            else:
                for _ in range(level_size):
                    node = s.pop()
                    levels[-1].append(node.val)
                    if node.right is not None:
                        s.appendleft(node.right)
                    if node.left is not None:
                        s.appendleft(node.left)
            
            start_from_left = not start_from_left
            
        
        return levels
```

### 二叉搜索树应用

### [validate-binary-search-tree](https://leetcode-cn.com/problems/validate-binary-search-tree/)

> 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

- 思路 1：中序遍历后检查输出是否有序，缺点是如果不平衡无法提前返回结果， 代码略

- 思路 2：分治法，一个二叉树为合法的二叉搜索树当且仅当左右子树为合法二叉搜索树且根结点值大于右子树最小值小于左子树最大值。缺点是若不用迭代形式实现则无法提前返回，而迭代实现右比较复杂。

```Python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root is None: return True
        
        def valid_min_max(node):
            
            isValid = True
            if node.left is not None:
                l_isValid, l_min, l_max = valid_min_max(node.left)
                isValid = isValid and node.val > l_max
            else:
                l_isValid, l_min = True, node.val

            if node.right is not None:
                r_isValid, r_min, r_max = valid_min_max(node.right)
                isValid = isValid and node.val < r_min
            else:
                r_isValid, r_max = True, node.val

                
            return l_isValid and r_isValid and isValid, l_min, r_max
        
        return valid_min_max(root)[0]
```

- 思路 3：利用二叉搜索树的性质，根结点为左子树的右边界，右子树的左边界，使用先序遍历自顶向下更新左右子树的边界并检查是否合法，迭代版本实现简单且可以提前返回结果。

```Python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        s = [(root, float('-inf'), float('inf'))]
        while len(s) > 0:
            node, low, up = s.pop()
            if node.left is not None:
                if node.left.val <= low or node.left.val >= node.val:
                    return False
                s.append((node.left, low, node.val))
            if node.right is not None:
                if node.right.val <= node.val or node.right.val >= up:
                    return False
                s.append((node.right, node.val, up))
        return True
```

#### [insert-into-a-binary-search-tree](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/)

> 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。

- 思路：如果只是为了完成任务则找到最后一个叶子节点满足插入条件即可。但此题深挖可以涉及到如何插入并维持平衡二叉搜索树的问题，并不适合初学者。

```Python
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            return TreeNode(val)
        
        node = root
        while True:
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
```

## 总结

- 掌握二叉树递归与非递归遍历
- 理解 DFS 前序遍历与分治法
- 理解 BFS 层次遍历

## 练习

- [ ] [maximum-depth-of-binary-tree](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
- [ ] [balanced-binary-tree](https://leetcode-cn.com/problems/balanced-binary-tree/)
- [ ] [binary-tree-maximum-path-sum](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)
- [ ] [lowest-common-ancestor-of-a-binary-tree](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [ ] [binary-tree-level-order-traversal](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
- [ ] [binary-tree-level-order-traversal-ii](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)
- [ ] [binary-tree-zigzag-level-order-traversal](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)
- [ ] [validate-binary-search-tree](https://leetcode-cn.com/problems/validate-binary-search-tree/)
- [ ] [insert-into-a-binary-search-tree](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/)
