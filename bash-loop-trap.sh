#!/bin/bash

trap 'stop_catch' INT

function stop_catch
{
  echo "breaking out of loop"
  STOP=1
}

STOP=0
while [ true ]; do
  if [ "$STOP" -eq 1 ]; then
    break
  fi
  echo "am loopink"
  sleep 1
done

echo "I am something that happens after the loop"
echo "I shouldn't be affected by the SIGINT signal"
