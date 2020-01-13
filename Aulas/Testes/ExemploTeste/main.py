def do_stuff(num=0):
  try:
    num = int(num)
    # try to test for when input is 0. How can you fix this?
    return num + 5
  except ValueError as err:
    print('please enter number')
    return err
  except TypeError as err:
    print('please enter number')
    return err

