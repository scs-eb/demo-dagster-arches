import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"demo_arches"), "demo_arches.urls", name="demo_arches"),
)
