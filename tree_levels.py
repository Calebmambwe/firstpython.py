# def tree_levels(root):
#     levels = []
#     _tree_levels(root, levels, 0)
#     return levels
#
#
# def _tree_levels(root, levels, level_num):
#     if root is None:
#         return
#
#     if level_num == len(levels):
#         levels.append([root.val])
#     else:
#         levels[level_num].append(root.val)
#
#     _tree_levels(root.left, levels, level_num + 1)
#     _tree_levels(root.right, levels, level_num + 1)

    def tree_levels(root):
        if root is None:
            return []

        levels = []
        queue = deque([(root, 0)])
        while queue:
            current, level_num = queue.popleft()

            if len(levels) == level_num:
                levels.append([current.val])
            else:
                levels[level_num].append(current.val)

            if current.left is not None:
                queue.append((current.left, level_num + 1))

            if current.right is not None:
                queue.append((current.right, level_num + 1))

        return levels