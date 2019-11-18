import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy
from scipy import ndimage
from PIL import Image
import pylab as mplt





class Measurements(object):

	def center_of_mass(self, data):
		cg = ndimage.measurements.center_of_mass(data)
		return cg



class MomentsMeasurments(object):

    	# info: https://alyssaq.github.io/2015/computing-the-axes-or-orientation-of-a-blob/

	def raw_moment(self, data, i_order, j_order):
		nrows, ncols = data.shape
		y_indices, x_indicies = np.mgrid[:nrows, :ncols]
		return (data * x_indicies**i_order * y_indices**j_order).sum()


	def moments_cov(self, data):
		data_sum = data.sum()
		m10 = self.raw_moment(data, 1, 0)
		m01 = self.raw_moment(data, 0, 1)
		x_centroid = m10 / data_sum
		y_centroid = m01 / data_sum
		u11 = (self.raw_moment(data, 1, 1) - x_centroid * m01) / data_sum
		u20 = (self.raw_moment(data, 2, 0) - x_centroid * m10) / data_sum
		u02 = (self.raw_moment(data, 0, 2) - y_centroid * m01) / data_sum
		cov = np.array([[u20, u11], [u11, u02]])
		return cov

	def moments(self, data):
		cov = self.moments_cov(data)
		evals, evecs = np.linalg.eig(cov)
		print(evals, evecs)
		return evals, evecs

	def rotation(self, data):
		evals, evecs = self.moments(data)
		sort_indices = np.argsort(evals)[::-1]
		x_v1, y_v1 = evecs[:, sort_indices[0]]
		x_v2, y_v2 = evecs[:, sort_indices[1]]
		theta = np.tanh((x_v1)/(y_v1))
		return theta

	def rotated_image(self, data, angle_rad):
		angle_deg = -1*np.rad2deg(np.tan(angle_rad))+90
		out = scipy.ndimage.interpolation.rotate(data, angle_deg)
		return out, angle_deg

if __name__ == "__main__":
    name = "0.tiff"
    PSF = mpimg.imread(name)

    im = Image.open('0.tiff')
    imarray = np.uint16(np.array(im))

    image = imarray[:,:,0]+imarray[:,:,1]+imarray[:,:,2]
    im = mplt.imshow(image, cmap='hot')
    mplt.show()
    PSF = image

    mea = Measurements()
    mom = MomentsMeasurments()
    
    normed_PSF = PSF/np.amax(PSF)*255
    trashold_PSF = (normed_PSF > 200) * normed_PSF
    
    center_of_gravity = mea.center_of_mass(trashold_PSF)
    print('center of gravity =', center_of_gravity)
    
    theta = mom.rotation(trashold_PSF)
    print('theta =', theta)
    
    rotated_PSF, angle_deg = mom.rotated_image(trashold_PSF, theta)
    print('theta_deg =', angle_deg)	
    
    plt.imshow(rotated_PSF)
    plt.show()
#    angles.append(round(angle_deg,0))

#compute("0.tiff")