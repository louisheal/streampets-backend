import queue


def format_sse(data: str, event=None) -> str:
  msg = f'data: {data}\n\n'
  if event is not None:
    msg = f'event: {event}\n{msg}'
  return msg

class MessageAnnouncer:

  def __init__(self) -> None:
    self.listeners = []

  def listen(self):
    q = queue.Queue()
    self.listeners.append(q)
    return q
  
  def announce(self, msg, event=None):
    msg = format_sse(msg, event)
    for i in reversed(range(len(self.listeners))):
      try:
        self.listeners[i].put_nowait(msg)
      except:
        del self.listeners[i]
