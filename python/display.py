import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

def plot(bars):
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111, aspect='equal')

    count = 0
    total = bars.index[-1]
    factor = 5
    while count <= total:
        open  = bars.loc[total - count, 'do'] * factor
        high  = bars.loc[total - count, 'dh'] * factor
        low   = bars.loc[total - count, 'dl'] * factor
        close = bars.loc[total - count, 'dc'] * factor

        body = math.fabs(close - open)
        shadow_tail = min(close, open) - low
        shadow_head = high - max(close, open)
        if close >= open:
            color = "green"
        else:
            color = "red"

        offset = count + (count * 0.5)

        # shadow_tail
        ax2.add_patch(
            patches.Rectangle(
                (offset + 0.5, low),
                0.01, shadow_tail,
                color=color,
                alpha=0.4,
                fill=True
            )
        )

        # body
        ax2.add_patch(
             patches.Rectangle(
                (offset + 0, shadow_tail + low),
                1, body,
                facecolor=color,
                edgecolor='black',
                alpha=0.8,
                fill=True
            )
        )

        # shadow_head
        ax2.add_patch(
            patches.Rectangle(
                (offset + 0.5, body + shadow_tail + low),
                0.01, shadow_head,
                color=color,
                alpha=0.4,
                fill=True
            )
        )
        count += 1

    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
