import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, aspect='equal')

high = 1
open = 0.2
close = 0.9
low = 0

body = math.fabs(close - open)
shadow_tail = body - low
shadow_head = high - body
if close >= open:
    color = "green"
else:
    color = "red"

offset = 100

# shadow_tail
ax2.add_patch(
    patches.Rectangle(
        (offset + 0.5, low),
        0.02, shadow_tail,
        color="black",
        fill=True
    )
)

# body
ax2.add_patch(
     patches.Rectangle(
        (offset + 0, shadow_low + low),
        1, body,
        color=color,
        fill=True
    )
)

# shadow_head
ax2.add_patch(
    patches.Rectangle(
        (offset + 0.5, body + shadow_low + low),
        0.02, shadow_head,
        color="black",
        fill=True
    )
)



plt.axis('equal')
plt.axis('off')
plt.tight_layout()
plt.show()
