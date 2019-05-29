import tensorflow as tf
# 导入库
hello = tf.constant('''hello, world!''')
# 创造一个变量，tensor里面的常量
# 一个计算图
node1=tf.constant(3.0, tf.float16,name='''node1''')
node2=tf.constant(4.0, tf.float16,name='''node2''')
node3=tf.add(node1,node2)
print(node3)
sess=tf.Session()
# 构造tensor的对话

print(sess.run(node3))
sess.close()