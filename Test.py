import tensorflow as tf
Input1=tf.placeholder('float',name="input_1")
Input2=tf.placeholder('float',name="input_2")
x=tf.Variable(0,dtype="float")
output=tf.Variable(0,dtype="float")

x=Input1*Input2
output=x*x

sess=tf.Session()
sess.run(output,feed_dict={Input1:3,Input2:4})