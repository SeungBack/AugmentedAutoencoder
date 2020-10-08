# Author: Tomas Hodan (hodantom@cmp.felk.cvut.cz)
# Center for Machine Perception, Czech Technical University in Prague

import numpy as np

def calc_2d_bbox(xs, ys, im_size, clip=False):
    bb_tl = [xs.min(), ys.min()]
    bb_br = [xs.max(), ys.max()]
    if clip:
        bb_tl = clip_pt_to_im(bb_tl, im_size)
        bb_br = clip_pt_to_im(bb_br, im_size)
    return [bb_tl[0], bb_tl[1], bb_br[0] - bb_tl[0], bb_br[1] - bb_tl[1]]


def depth_im_to_dist_im(depth_im, K):
    """
    Converts depth image to distance image.
    :param depth_im: Input depth image, where depth_im[y, x] is the Z coordinate
    of the 3D point [X, Y, Z] that projects to pixel [x, y], or 0 if there is
    no such 3D point (this is a typical output of the Kinect-like sensors).
    :param K: Camera matrix.
    :return: Distance image dist_im, where dist_im[y, x] is the distance from
    the camera center to the 3D point [X, Y, Z] that projects to pixel [x, y],
    or 0 if there is no such 3D point.
    """
    xs = np.tile(np.arange(depth_im.shape[1]), [depth_im.shape[0], 1])
    ys = np.tile(np.arange(depth_im.shape[0]), [depth_im.shape[1], 1]).T

    Xs = np.multiply(xs - K[0, 2], depth_im) * (1.0 / K[0, 0])
    Ys = np.multiply(ys - K[1, 2], depth_im) * (1.0 / K[1, 1])

    dist_im = np.linalg.norm(np.dstack((Xs, Ys, depth_im)), axis=2)
    return dist_im