

def XmasTree(height):
  # 0. line width - DONE

  # 1. Leaves of tree
    # loop through numbers from 1 to height (inclusive) - call it n
      # find what leaves looks like on that level: two args, line width, n
      # store it
    

  # 2. Tree trunk - DONE
    # find half the trunk fn(line width)
    # repeat it

  # THEN: stitch results of 1 and 2 together

  pass

def find_line_width(height):
  return 2 * height - 1
  # pass

def find_tree_trunk(height):
  half_trunk_width = height - 1
  half_trunk_padding = '_' * half_trunk_width
  one_trunk_level = f"{half_trunk_padding}#{half_trunk_padding}"
  return [one_trunk_level, one_trunk_level]

def test_find_line_width():
  assert find_line_width(5) == 9
  assert find_line_width(3) == 5

def test_find_tree_trunk():
  assert find_tree_trunk(5) == ['____#____', '____#____']
  assert find_tree_trunk(3) == ['__#__', '__#__']



