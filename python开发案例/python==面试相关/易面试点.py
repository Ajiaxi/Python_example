# coding = utf-8
__author__ = 'super_fazai'
# @Time    : 17-7-29 ����10:08
# @File    : �����Ե�.py

# 1. �мǲ�Ҫ�߱���, ����ɾ, �������©(����ѭ��ʱ�޸��б�)
a = [11, 22, 33, 44, 55, 66]

for i in a:     # ��ʧԪ��44
    print(i)
    if i == 33:
        a.remove(i)
print(a)
print('')


a = [11, 22, 33, 44, 55, 66]
# �߱�����ɾ���б�Ԫ�ص�һ�㲽��
# �������: �ȴ�����ʱ�б�,���ڼ�¼Ҫɾ����Ԫ��,�ٱ�����ʱ�б�ɾ��,����ԭ�б���ɾ��
tmp = []
for i in a:
    if i == 33:
        tmp.append(i)
i = 0
for j in tmp:
    if i >0 and i < len(a)-1:
        print(a[i])
    else:
        break
    i += 1
    a.remove(j)

print(a)

print('�ָ���'.center(40, '-'))

# 2. �мǲ�Ҫʹ�ÿɱ��������Ϊ������Ĭ�ϲ���
# ������ϣ��ÿ�ε��øú���ʱ���ᴴ��һ���µ��б������ṩĬ�ϲ����Ĳ���
# �����������ˣ�Python���ڵ�һ�ζ��庯��ʱ�����ɱ����Ĭ�ϲ��������ǵ���������ʱ

# ��1:
def append_to_list(value, def_list=[]):
    def_list.append(value)
    return def_list

my_list = append_to_list(1)
print(my_list)

my_other_list = append_to_list(2)
print(my_other_list)

# ��2:
# ��һ���ܺõ����ӱ����������������������ǵ�����ʱ������Ĭ�ϲ�����
import time
def report_arg(my_default=time.time()):
    print(my_default)

report_arg()

time.sleep(2)

report_arg()

print('�ָ���'.center(40, '-'))

# ע��������������
# ע���ڽ�'in'��������������ʱ�������������Ϊһ��һ��λ�ñ������ġ������ǾͲ����һ��ʼ�ͽ�������
# ���ǿ��Խ���ת��Ϊlist �������������
gen = (i for i in range(5))
print('2 in gen,', 2 in gen)        # True
print('3 in gen,', 3 in gen)        # True
print('1 in gen,', 1 in gen)        # False

# �����������������������Ŀ�ģ��ڴ��������£������ǿ��Խ�һ�������ת����һ���б�������������
gen = (i for i in range(5))
gen = list(gen)
print('2 in gen,', 2 in gen)        # True
print('3 in gen,', 3 in gen)        # True
print('1 in gen,', 1 in gen)        # True

print('�ָ���'.center(40, '-'))

# bool��int������
print('isinstance(True, int):', isinstance(True, int))      # True
print('True + True:', True + True)                          # 2
print('3*True + True:', 3*True + True)                      # 4
print('3*True - False:', 3*True - False)                    # 3

# ����lambda-in-closures-and-a-loop����

print('�ָ���'.center(40, '-'))

# ����ע�� '->' �ҵ�python������ʲô?
'''
����û�п����κ�Python�����ں��������parantheses��ʹ��ð�ţ�
'''
'''def foo1(x: 'insert x here', y: 'insert x^2 here'):
    print('Hello, World')
    return'''
def foo2(x, y) -> 'Hi!':
    print('Hello, World')
    return
'''
�ʣ�������Ч��Python�﷨��
A���ǵ�

�ʣ���ô����Ҹոյ��ú�������ô����
A��ûʲô��

����֤����
'''
foo1(1, 2)
foo2(1, 2)
print(foo1.__annotations__)
print(foo2.__annotations__)
'''
**���ԣ���Щ�Ǻ���ע��... **

ð�ŵĹ��ܲ���
����ֵ�ļ�ͷ
�������Զ����ʹ�����ǣ������ٺ��٣���ͨ���������ں�������дһ���ܺõĺ����ĵ���Ϊһ��docstring - �����������Ҹ���ô��
'''

