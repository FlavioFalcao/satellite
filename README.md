# Insights
There are two ideas in my heat. The key difference of the two is whether to
open up `trace_on` mode of rabbitmq. 

The first one, which using this mode, we can get more detail information about 
message, includes when cast/call a not-specified host request, we can know 
which consumer got the message. In this way we can get verbose debug 
information. But the mode is more match debuging with nova-network, because 
nova-compute always make server-specified request, which means I always know 
which host receive the request, so no need to trace on. When using nova-network 
in `multi_host` mode, a request will send to a no-specified host, but will 
re-send to correct host, even if the mode is turn off, we can parse message 
body to know the first station is who, which I think is not too bad. If luck
enough, the message first station is correct host, we will know nothing about
that, and we may find the will be a bug.

# Roadmap
  1. trace_off, for easier debuging for nova-compute. And take some experiment
  2. trace_on, for easier debuging for nova-network.

# References
  -. http://www.rabbitmq.com/firehose.html
  -. http://www.rabbitmq.com/tutorials/tutorial-five-python.html
