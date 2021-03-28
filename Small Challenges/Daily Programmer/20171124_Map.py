# This is extremely sloppy.
# There are so many redundant operations and it's mostly checks
# But ultimately it's a quick and simple script that gets the job done

def get_map(size, path):
  minx = size
  miny = size
  maxx = 0
  maxy = 0

  # Find maxes and mins
  for point in path:
    minx = min(point[0], minx)
    maxx = max(point[0], maxx)
    miny = min(point[1], miny)
    maxy = max(point[1], maxy)

  # Attempt to pad out
  minx = max(0, minx-30)
  maxx = min(size, maxx + 30)
  miny = max(0, miny-30)
  maxy = min(size, maxy+30)

  # Find max difference and find new co-ordinates based on it
  max_diff = max(maxx-minx, maxy-miny)
  minx = ((maxx+minx)/2)-(max_diff/2)
  maxx = minx+max_diff
  miny = ((maxy+miny)/2)-(max_diff/2)
  maxy = miny+max_diff

  # Shift and truncate co-ordiantes which are out of bounds
  if minx < 0:
    maxx = min(size, maxx + abs(minx))
    minx = 0
  if maxx > size:
    minx = max(0,minx-(maxx-size))
    maxx = size
  if miny < 0:
    maxy = min(size, maxy + abs(miny))
    miny = 0
  if maxy > size:
    miny = max(0,miny-(maxy-size))
    maxy = size
  
  # Print minima and box size
  print(str((int(minx), int(miny))) + ', ' + str(max_diff))

if __name__ == "__main__":
  # Example tests
  get_map(2000, [(600, 600), (700, 1200)])
  #get_map(2000, [(300, 300), (1300, 300)])
  #get_map(2000, [(825, 820), (840, 830), (830, 865), (835, 900)])
  #get_map(5079, [(5079, 2000), (5079, 3000)])
  #get_map(5079, [(1000, 0), (1000, 5079)])
  #eval("get_map("+input()+")") # custom map that can be tested
