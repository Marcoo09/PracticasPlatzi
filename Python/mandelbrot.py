import tensorflow as tf
import numpy as np
from PIL import Image

R = 4
ITER_NUM = 200

def color(z,i):
    if abs(z) < R:
        return 0,0,0
    v = np.log2(i + R - np.log2(np.log2(abs(z)))) / 5
    if v < 1.0:
        return v **6, v**2.9, v
    else:
        v = max(0, 2 - v)
        return v,v**3,v**3


def gen_mandelbrot(Z):
    xs = tf.constant(Z.astype(np.complex64)) #astype castea la variable z a complex64 (lo que se le pasa por parámetro)
    zs = tf.Variable(xs)
    ns = tf.Variable(tf.zeros_like(xs,tf.float32)) #zeros_like return an array of zeros withe the same shape  (forma) and type of the given array
    with tf.Session():
        tf.global_variables_initializer().run()
        zs_ = tf.where(tf.abs(zs) < R, zs**2 + xs, zs) #tf.where recieves four parameteres, the conditions, a Tensor which have the same shape to the condition, other tensor, name
        not_diverged = tf.abs(zs_) < R
        step = tf.group(
            zs.assign(zs_),
            ns.assign_add(tf.cast(not_diverged,tf.float32))
            )
        for i in range(ITER_NUM):
            step.run()
        final_step = ns.eval()
        final_z = zs.eval()
    r,g,b = np.frompyfunc(color,2,3)(final_z, final_step)
    img_array = np.dstack((r,g,b))
    return Image.fromarray(np.uint8(img_array * 255))

if __name__ == "__main__":
    start_x = -2.5 #X range
    end_x = 1
    start_y = -1.2 # Y range
    end_y = 1.2
    width = 1500 #image width

    step = (end_x - start_x) / width
    Y,X = np.mgrid[start_y:end_y:step,start_x:end_x:step]
    Z = X + 1j * Y

    img = gen_mandelbrot(Z)
    img.save('Marco4.png')