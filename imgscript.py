import os   # handling files
import cv2  # for converting gray scale
import sys  # for handling command arguments
import shutil  # for removing entire folder/directory


def make_stuff(input_dir, output_dir):

	count = 1

	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)

	for image_name in os.listdir(input_dir):
		if '.txt' in image_name:
			continue


		print( str(count) + '.', image_name, end='   -->>>  ')	

		image_abs_path = os.path.join(input_dir, image_name)

		image_array = cv2.imread( image_abs_path )

		gray_image_array =  cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

		output_image_abs_path = os.path.join(output_dir, image_name)

		status = cv2.imwrite( output_image_abs_path, gray_image_array)
		if status:
			print('success', end='\n\n')
		else:
			print('failed', end='\n\n')

		count += 1

if __name__ == '__main__':
	input_dir = sys.argv[1]
	output_dir = sys.argv[2]

	make_stuff(input_dir, output_dir)
