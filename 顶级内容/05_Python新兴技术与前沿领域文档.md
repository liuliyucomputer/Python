# Python新兴技术与前沿领域文档

## 1. 量子计算与量子编程

### 1.1 量子计算基础概念
**[标识: QUANTUM-COMPUTING-001]**

量子计算是利用量子力学原理进行信息处理的新型计算方式，具有解决某些经典计算机难以处理的问题的潜力。

```python
# 量子计算基础概念示例

# 量子比特（Qubit）的概念理解
# 经典比特: 0 或 1
# 量子比特: 可以同时处于0和1的叠加态

# 量子纠缠（Entanglement）的理解
# 两个或多个量子比特之间的强相关性

# 量子门操作的基本类型
# - 单量子比特门: Pauli-X, Pauli-Y, Pauli-Z, Hadamard等
# - 多量子比特门: CNOT, Toffoli等
```

### 1.2 Python量子计算框架
**[标识: QUANTUM-FRAMEWORK-001]**

使用Python进行量子计算开发的主流框架和库。

```python
# Qiskit (IBM的量子计算框架)

# 安装: pip install qiskit qiskit-visualization

from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.visualization import plot_histogram

# 创建一个简单的量子电路（Bell态）
qc = QuantumCircuit(2, 2)
qc.h(0)  # Hadamard门作用在第一个量子比特上
qc.cx(0, 1)  # CNOT门，控制比特是0，目标比特是1
qc.measure([0, 1], [0, 1])  # 测量量子比特并映射到经典比特

# 绘制电路
print("量子电路图:")
print(qc.draw())

# 使用模拟器运行电路
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(qc)

# 绘制结果直方图
print("\n测量结果:")
print(counts)

# 示例：QAOA算法（量子近似优化算法）解决最大割问题

# PennyLane（跨平台量子计算框架）

# 安装: pip install pennylane pennylane-qiskit pennylane-lightning

import pennylane as qml
from pennylane import numpy as np

# 创建量子设备
dev = qml.device("default.qubit", wires=2)

# 定义量子电路（量子节点）
@qml.qnode(dev)

def circuit(phi):
    # 初始化
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    # 参数化旋转门
    qml.RX(phi, wires=0)
    # 测量
    return qml.expval(qml.PauliZ(0))

# 优化参数
phi = 0.5
result = circuit(phi)
print(f"\nPennyLane电路结果: {result}")

# Cirq (Google的量子计算框架)

# 安装: pip install cirq

import cirq

# 创建量子比特
q0, q1 = cirq.LineQubit.range(2)

# 创建电路
circuit = cirq.Circuit()
# 添加门
circuit.append(cirq.H(q0))  # Hadamard门
circuit.append(cirq.CNOT(q0, q1))  # CNOT门
circuit.append(cirq.measure(q0, q1, key='result'))  # 测量

print("\nCirq电路图:")
print(circuit)

# 模拟运行
 simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1000)
print("\nCirq测量结果:")
print(result.histogram(key='result'))
```

### 1.3 量子算法与应用场景
**[标识: QUANTUM-ALGORITHM-001]**

探索Python实现的量子算法及其在不同领域的应用。

```python
# 量子傅里叶变换（QFT）

from qiskit import QuantumCircuit

def qft_rotations(circuit, n):
    """QFT算法的旋转部分"""
    if n == 0:  # 基本情况
        return circuit
    n -= 1  # 索引从0开始
    circuit.h(n)
    for qubit in range(n):
        circuit.cp(np.pi/2**(n-qubit), qubit, n)
    # 递归应用到剩余的量子比特
    qft_rotations(circuit, n)

def swap_registers(circuit, n):
    """交换寄存器以完成QFT"""
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    return circuit

def qft(circuit, n):
    """创建n量子比特的QFT"""
    qft_rotations(circuit, n)
    swap_registers(circuit, n)
    return circuit

# 创建QFT电路
n = 3
qft_circuit = QuantumCircuit(n)
qft(qft_circuit, n)
print("\n量子傅里叶变换电路图:")
print(qft_circuit.draw())

# Shor算法（用于因数分解）思想展示
"""
Shor算法的主要步骤：
1. 选择一个随机数a < N
2. 计算gcd(a, N)，如果不等于1，则找到一个因数
3. 使用量子傅里叶变换寻找a^x mod N的周期r
4. 如果r为偶数且a^(r/2) ≠ -1 mod N，则gcd(a^(r/2) ± 1, N)可能是N的因数
"""

# Grover搜索算法

from qiskit import Aer, execute

def create_oracle(n, marked_states):
    """创建Grover搜索的oracle"""
    qc = QuantumCircuit(n)
    # 对每个标记状态添加相位翻转
    for state in marked_states:
        # 将二进制状态转换为整数索引
        binary_state = format(state, '0' + str(n) + 'b')[::-1]  # 反转以便先处理低位
        
        # 添加X门到二进制状态中为0的位置
        for i in range(n):
            if binary_state[i] == '0':
                qc.x(i)
        
        # 添加多控Z门
        qc.h(n-1)
        qc.mcx(list(range(n-1)), n-1)  # 多控X门作为Z门使用
        qc.h(n-1)
        
        # 撤销X门
        for i in range(n):
            if binary_state[i] == '0':
                qc.x(i)
    
    return qc

def create_diffusion(n):
    """创建Grover搜索的扩散算子"""
    qc = QuantumCircuit(n)
    # 应用H门到所有量子比特
    for qubit in range(n):
        qc.h(qubit)
    # 应用X门到所有量子比特
    for qubit in range(n):
        qc.x(qubit)
    # 应用多控Z门
    qc.h(n-1)
    qc.mcx(list(range(n-1)), n-1)
    qc.h(n-1)
    # 应用X门到所有量子比特
    for qubit in range(n):
        qc.x(qubit)
    # 应用H门到所有量子比特
    for qubit in range(n):
        qc.h(qubit)
    return qc

def grover_algorithm(n, marked_states, iterations):
    """实现Grover搜索算法"""
    # 创建电路
    qc = QuantumCircuit(n, n)
    
    # 初始化叠加态
    for qubit in range(n):
        qc.h(qubit)
    
    # 创建oracle和diffusion算子
    oracle = create_oracle(n, marked_states)
    diffusion = create_diffusion(n)
    
    # 重复Grover迭代
    for _ in range(iterations):
        qc.compose(oracle, inplace=True)
        qc.compose(diffusion, inplace=True)
    
    # 测量
    qc.measure(list(range(n)), list(range(n)))
    
    return qc

# 示例：在3量子比特系统中搜索状态|101⟩
n = 3
marked_states = [5]  # |101⟩对应的十进制是5
iterations = 1  # 迭代次数 ~π/4*sqrt(N/M)

grover_circuit = grover_algorithm(n, marked_states, iterations)
print("\nGrover搜索算法电路图:")
print(grover_circuit.draw())

# 运行模拟
simulator = Aer.get_backend('qasm_simulator')
job = execute(grover_circuit, simulator, shots=1000)
result = job.result()
counts = result.get_counts()
print("\nGrover搜索结果:")
print(counts)

# 量子机器学习应用示例

# 安装: pip install pennylane pennylane-qiskit scikit-learn

import pennylane as qml
from pennylane import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 创建量子设备
dev = qml.device("default.qubit", wires=2)

# 定义量子电路（量子神经网络）
@qml.qnode(dev)
def qnn_circuit(weights, x):
    # 数据编码
    qml.RX(x[0], wires=0)
    qml.RY(x[1], wires=0)
    qml.CNOT(wires=[0, 1])
    
    # 参数化层
    qml.Rot(weights[0, 0], weights[0, 1], weights[0, 2], wires=0)
    qml.Rot(weights[1, 0], weights[1, 1], weights[1, 2], wires=1)
    
    # 测量
    return qml.expval(qml.PauliZ(1))

# 定义成本函数
def cost_function(weights, X, y):
    predictions = [qnn_circuit(weights, x) for x in X]
    return np.mean((predictions - y) ** 2)

# 准备数据
X, y = make_moons(n_samples=100, noise=0.1, random_state=42)
y = np.where(y == 0, -1, 1)  # 将0-1标签转换为-1-1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 数据标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 初始化权重
np.random.seed(42)
weights = np.random.random((2, 3))

# 优化器
opt = qml.GradientDescentOptimizer(stepsize=0.1)

# 训练
steps = 100
for i in range(steps):
    weights = opt.step(lambda w: cost_function(w, X_train, y_train), weights)
    if (i + 1) % 10 == 0:
        cost = cost_function(weights, X_train, y_train)
        print(f"步骤 {i+1}/{steps}, 成本: {cost:.4f}")

# 评估模型
def predict(weights, x):
    return np.sign(qnn_circuit(weights, x))

y_pred = [predict(weights, x) for x in X_test]
accuracy = np.mean(y_pred == y_test)
print(f"\n测试准确率: {accuracy:.4f}")
```

## 2. 边缘计算与物联网

### 2.1 边缘AI与轻量级机器学习
**[标识: EDGE-AI-001]**

在资源受限的边缘设备上部署Python轻量级机器学习模型。

```python
# 使用TensorFlow Lite进行模型量化和边缘部署

# 安装: pip install tensorflow

import tensorflow as tf
import numpy as np

# 创建一个简单的模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# 编译模型
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 生成虚拟数据
X_train = np.random.random((1000, 10))
y_train = np.random.randint(0, 2, (1000, 1))

# 训练模型
model.fit(X_train, y_train, epochs=5, batch_size=32)

# 保存原始模型
model.save('original_model.h5')

# 转换为TFLite模型
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# 启用整数量化
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# 使用代表性数据集进行量化
# 创建一个生成器提供代表性数据
def representative_data_gen():
    for i in range(50):
        yield [X_train[i:i+1].astype(np.float32)]

# 设置代表性数据集
converter.representative_dataset = representative_data_gen

# 设置推理输入输出的类型（必须是量化模型）
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8

# 转换模型
tflite_quant_model = converter.convert()

# 保存TFLite模型
with open('quantized_model.tflite', 'wb') as f:
    f.write(tflite_quant_model)

print("原始模型大小:", len(tf.io.read_file('original_model.h5')) / 1024, "KB")
print("量化模型大小:", len(tflite_quant_model) / 1024, "KB")

# 使用ONNX Runtime进行跨平台部署

# 安装: pip install onnx onnxruntime

import onnx
from onnx import numpy_helper
import onnxruntime as rt

# 转换为ONNX格式
import tf2onnx

# 转换模型
onnx_model, _ = tf2onnx.convert.from_keras(model, input_signature=[tf.TensorSpec(shape=[None, 10], dtype=tf.float32, name='input')], opset=13)

# 保存ONNX模型
with open('model.onnx', 'wb') as f:
    f.write(onnx_model.SerializeToString())

print("ONNX模型大小:", len(onnx_model.SerializeToString()) / 1024, "KB")

# 使用ONNX Runtime进行推理
sess = rt.InferenceSession('model.onnx')
input_name = sess.get_inputs()[0].name
output_name = sess.get_outputs()[0].name

# 测试推理
input_data = np.random.random((1, 10)).astype(np.float32)
result = sess.run([output_name], {input_name: input_data})
print("ONNX推理结果:", result)

# 使用PyTorch Mobile进行模型优化

# 安装: pip install torch torchvision

import torch
import torch.nn as nn
import torch.optim as optim

# 定义PyTorch模型
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(10, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.sigmoid(self.fc3(x))
        return x

# 初始化模型
pytorch_model = SimpleModel()

# 保存模型
torch.save(pytorch_model.state_dict(), 'pytorch_model.pth')

# 转换为TorchScript格式
scripted_model = torch.jit.script(pytorch_model)
scripted_model.save('scripted_model.pt')

# 模型量化（动态量化）
quantized_model = torch.quantization.quantize_dynamic(
    pytorch_model,
    {nn.Linear},
    dtype=torch.qint8
)

# 保存量化模型
torch.jit.save(torch.jit.script(quantized_model), 'quantized_pytorch_model.pt')

print("PyTorch模型量化完成")

# 边缘设备上的推理优化技术

# 1. 模型剪枝示例
"""
# 安装: pip install torch-pruning

import torch_pruning as tp

# 加载预训练模型
model = SimpleModel()

# 定义剪枝策略
strategy = tp.strategy.L1Strategy()  # L1范数策略

# 初始化剪枝器
pruner = tp.pruner.MagnitudePruner(
    model,
    [(model.fc1, 'weight')],  # 要剪枝的层和参数
    strategy=strategy,
    pruning_ratio=0.5,  # 剪枝50%的权重
)

# 执行剪枝
pruner.step()

# 保存剪枝后的模型
torch.jit.save(torch.jit.script(model), 'pruned_model.pt')
"""

# 2. 知识蒸馏示例

class StudentModel(nn.Module):
    def __init__(self):
        super(StudentModel, self).__init__()
        self.fc1 = nn.Linear(10, 32)  # 更小的隐藏层
        self.fc2 = nn.Linear(32, 1)  # 直接输出
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x

# 知识蒸馏损失函数
def distillation_loss(student_logits, teacher_logits, target, T=2.0, alpha=0.5):
    # 软目标损失（KL散度）
    soft_targets = nn.functional.softmax(teacher_logits / T, dim=1)
    soft_prob = nn.functional.log_softmax(student_logits / T, dim=1)
    soft_loss = nn.functional.kl_div(soft_prob, soft_targets, reduction='batchmean') * (T * T)
    
    # 硬目标损失
    hard_loss = nn.functional.cross_entropy(student_logits, target)
    
    # 结合损失
    return alpha * soft_loss + (1 - alpha) * hard_loss

print("知识蒸馏模型定义完成")
```

### 2.2 物联网数据采集与处理
**[标识: IoT-DATA-001]**

使用Python进行物联网设备数据采集、传输和处理的最佳实践。

```python
# MQTT协议通信示例

# 安装: pip install paho-mqtt

import paho.mqtt.client as mqtt
import time
import json
import random

# MQTT代理设置
MQTT_BROKER = "broker.hivemq.com"  # 公共MQTT代理
MQTT_PORT = 1883
MQTT_CLIENT_ID = "python_iot_publisher"
MQTT_USERNAME = "your_username"  # 如果需要认证
MQTT_PASSWORD = "your_password"  # 如果需要认证

# 主题设置
MQTT_TOPIC_TEMPERATURE = "sensors/temperature"
MQTT_TOPIC_HUMIDITY = "sensors/humidity"
MQTT_TOPIC_DEVICE_STATUS = "devices/status"

# 发布者代码示例

def on_connect_publisher(client, userdata, flags, rc):
    if rc == 0:
        print("已连接到MQTT代理")
    else:
        print(f"连接失败，错误代码: {rc}")

# 创建MQTT客户端
publisher = mqtt.Client(client_id=MQTT_CLIENT_ID)

# 设置回调函数
publisher.on_connect = on_connect_publisher

# 设置认证信息（如果需要）
# publisher.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# 连接到代理
publisher.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)

# 启动循环
publisher.loop_start()

# 模拟传感器数据发布
try:
    print("开始发布传感器数据（按Ctrl+C停止）")
    while True:
        # 模拟温度数据
        temperature_data = {
            "device_id": "temp_sensor_01",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": round(random.uniform(20.0, 30.0), 2),
            "unit": "°C"
        }
        
        # 模拟湿度数据
        humidity_data = {
            "device_id": "hum_sensor_01",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "humidity": round(random.uniform(30.0, 70.0), 2),
            "unit": "%"
        }
        
        # 设备状态
        status_data = {
            "device_id": "device_01",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "online",
            "battery": round(random.uniform(70.0, 100.0), 1)
        }
        
        # 发布消息
        publisher.publish(MQTT_TOPIC_TEMPERATURE, json.dumps(temperature_data), qos=1)
        publisher.publish(MQTT_TOPIC_HUMIDITY, json.dumps(humidity_data), qos=1)
        publisher.publish(MQTT_TOPIC_DEVICE_STATUS, json.dumps(status_data), qos=1)
        
        print(f"发布温度数据: {temperature_data['temperature']}°C")
        print(f"发布湿度数据: {humidity_data['humidity']}%")
        print(f"发布设备状态: {status_data['status']}, 电池: {status_data['battery']}%")
        
        # 等待5秒
        time.sleep(5)
except KeyboardInterrupt:
    print("停止发布")
finally:
    # 停止循环并断开连接
    publisher.loop_stop()
    publisher.disconnect()

# 订阅者代码示例

# MQTT订阅客户端

MQTT_CLIENT_ID_SUBSCRIBER = "python_iot_subscriber"

# 接收消息回调函数
def on_message(client, userdata, msg):
    try:
        # 解析JSON消息
        payload = json.loads(msg.payload.decode())
        print(f"\n收到主题: {msg.topic}")
        print(f"消息内容: {json.dumps(payload, indent=2)}")
        
        # 根据主题进行不同的处理
        if msg.topic == MQTT_TOPIC_TEMPERATURE:
            # 温度数据处理逻辑
            temperature = payload["temperature"]
            if temperature > 28.0:
                print(f"警告: 温度过高 ({temperature}°C)")
        elif msg.topic == MQTT_TOPIC_HUMIDITY:
            # 湿度数据处理逻辑
            humidity = payload["humidity"]
            if humidity < 40.0:
                print(f"警告: 湿度过低 ({humidity}%)")
        elif msg.topic == MQTT_TOPIC_DEVICE_STATUS:
            # 设备状态处理逻辑
            status = payload["status"]
            battery = payload["battery"]
            if battery < 80.0:
                print(f"警告: 设备电池电量低 ({battery}%)")
                
    except Exception as e:
        print(f"处理消息时出错: {e}")

def on_connect_subscriber(client, userdata, flags, rc):
    if rc == 0:
        print("已连接到MQTT代理")
        # 订阅主题
        client.subscribe([
            (MQTT_TOPIC_TEMPERATURE, 1),
            (MQTT_TOPIC_HUMIDITY, 1),
            (MQTT_TOPIC_DEVICE_STATUS, 1)
        ])
        print("已订阅所有传感器主题")
    else:
        print(f"连接失败，错误代码: {rc}")

# 创建订阅客户端
subscriber = mqtt.Client(client_id=MQTT_CLIENT_ID_SUBSCRIBER)

# 设置回调函数
subscriber.on_connect = on_connect_subscriber
subscriber.on_message = on_message

# 设置认证信息（如果需要）
# subscriber.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# 连接到代理
subscriber.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)

# 开始订阅循环
print("开始接收消息（按Ctrl+C停止）")
try:
    subscriber.loop_forever()
except KeyboardInterrupt:
    print("停止订阅")
finally:
    subscriber.disconnect()

# 物联网数据处理管道

# 安装: pip install pandas matplotlib paho-mqtt

import pandas as pd
import matplotlib.pyplot as plt
from collections import deque

# 实时数据处理类
class IoTDataProcessor:
    def __init__(self, max_data_points=100):
        # 使用双端队列存储最近的数据点
        self.temperature_data = deque(maxlen=max_data_points)
        self.humidity_data = deque(maxlen=max_data_points)
        self.timestamps = deque(maxlen=max_data_points)
        
        # 数据统计
        self.temp_stats = {
            "min": float('inf'),
            "max": float('-inf'),
            "avg": 0.0,
            "count": 0
        }
        
        self.humidity_stats = {
            "min": float('inf'),
            "max": float('-inf'),
            "avg": 0.0,
            "count": 0
        }
    
    def process_temperature(self, value, timestamp):
        """处理温度数据"""
        # 添加到队列
        self.temperature_data.append(value)
        self.timestamps.append(timestamp)
        
        # 更新统计信息
        self.temp_stats["count"] += 1
        self.temp_stats["min"] = min(self.temp_stats["min"], value)
        self.temp_stats["max"] = max(self.temp_stats["max"], value)
        # 移动平均计算
        self.temp_stats["avg"] = (
            (self.temp_stats["avg"] * (self.temp_stats["count"] - 1) + value) / 
            self.temp_stats["count"]
        )
        
        # 简单异常检测
        if value > 30.0 or value < 10.0:
            return f"异常: 温度值 {value}°C 超出正常范围"
        
        return None
    
    def process_humidity(self, value, timestamp):
        """处理湿度数据"""
        # 添加到队列
        self.humidity_data.append(value)
        
        # 更新统计信息
        self.humidity_stats["count"] += 1
        self.humidity_stats["min"] = min(self.humidity_stats["min"], value)
        self.humidity_stats["max"] = max(self.humidity_stats["max"], value)
        # 移动平均计算
        self.humidity_stats["avg"] = (
            (self.humidity_stats["avg"] * (self.humidity_stats["count"] - 1) + value) / 
            self.humidity_stats["count"]
        )
        
        # 简单异常检测
        if value > 90.0 or value < 10.0:
            return f"异常: 湿度值 {value}% 超出正常范围"
        
        return None
    
    def get_statistics(self):
        """获取当前统计信息"""
        return {
            "temperature": self.temp_stats.copy(),
            "humidity": self.humidity_stats.copy(),
            "data_points": len(self.temperature_data)
        }
    
    def visualize_data(self, save_path=None):
        """可视化最近的数据"""
        if len(self.timestamps) < 2:
            print("数据点不足，无法可视化")
            return
        
        # 创建数据框
        df = pd.DataFrame({
            'timestamp': list(self.timestamps),
            'temperature': list(self.temperature_data),
            'humidity': list(self.humidity_data)
        })
        
        # 设置时间戳为索引
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)
        
        # 创建图表
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        # 绘制温度
        ax1.set_xlabel('时间')
        ax1.set_ylabel('温度 (°C)', color='tab:red')
        ax1.plot(df.index, df['temperature'], color='tab:red', marker='o', linestyle='-', markersize=4)
        ax1.tick_params(axis='y', labelcolor='tab:red')
        
        # 创建第二个Y轴绘制湿度
        ax2 = ax1.twinx()
        ax2.set_ylabel('湿度 (%)', color='tab:blue')
        ax2.plot(df.index, df['humidity'], color='tab:blue', marker='s', linestyle='--', markersize=4)
        ax2.tick_params(axis='y', labelcolor='tab:blue')
        
        # 设置标题
        plt.title('实时传感器数据监控')
        
        # 调整布局
        fig.tight_layout()
        
        # 保存或显示图表
        if save_path:
            plt.savefig(save_path, dpi=300)
            print(f"图表已保存到 {save_path}")
        else:
            plt.show()

# 使用示例
# processor = IoTDataProcessor()
# for i in range(20):
#     temp = 25 + random.uniform(-2, 2)
#     humidity = 50 + random.uniform(-10, 10)
#     timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
#     
#     temp_alert = processor.process_temperature(temp, timestamp)
#     humidity_alert = processor.process_humidity(humidity, timestamp)
#     
#     if temp_alert:
#         print(temp_alert)
#     if humidity_alert:
#         print(humidity_alert)
#     
#     time.sleep(0.5)
# 
# # 获取统计信息
# stats = processor.get_statistics()
# print("\n统计信息:")
# print(json.dumps(stats, indent=2))
# 
# # 可视化数据
# processor.visualize_data("sensor_data.png")

# LoRaWAN协议通信示例（模拟）

"""
# 安装: pip install pycryptodome

from Crypto.Cipher import AES
import base64
import struct

def generate_lorawan_payload(device_id, data):
    """模拟生成LoRaWAN加密有效载荷"""
    # 这里仅作为示例，实际LoRaWAN通信需要完整的OTAA或ABP认证
    # 以及正确的AES加密和MIC计算
    
    # 模拟设备地址
    dev_addr = bytes.fromhex("01234567")
    
    # 模拟FCtrl和FCnt
    f_ctrl = 0x80  # ADR位设置
    f_cnt = 123    # 帧计数器
    
    # 数据内容（温度和湿度作为示例）
    temp = int(data.get("temperature", 25) * 10)
    humidity = int(data.get("humidity", 50))
    
    # 将数据打包为二进制
    payload = struct.pack("!hB", temp, humidity)
    
    # 模拟加密（实际应用中需要正确的AES-128加密）
    # 这里仅作演示
    
    print(f"LoRaWAN数据包生成:")
    print(f"  设备ID: {device_id}")
    print(f"  设备地址: {dev_addr.hex()}")
    print(f"  帧计数器: {f_cnt}")
    print(f"  原始数据: {payload.hex()}")
    
    return {
        "dev_addr": dev_addr.hex(),
        "f_cnt": f_cnt,
        "payload": base64.b64encode(payload).decode(),
        "device_id": device_id
    }

# 使用示例
lorawan_data = generate_lorawan_payload(
    "lora_device_01",
    {"temperature": 26.5, "humidity": 62}
)
print(json.dumps(lorawan_data, indent=2))
"""
```

### 2.3 实时数据处理与边缘分析
**[标识: EDGE-ANALYTICS-001]**

在边缘设备上实现实时数据分析和处理算法。

```python
# 使用Numba进行实时数据处理优化

# 安装: pip install numba

import numpy as np
from numba import jit, njit, prange
import time

# 生成测试数据
np.random.seed(42)
data = np.random.rand(1_000_000)

# 传统Python函数
def calculate_moving_average_python(data, window_size):
    """使用Python标准方法计算移动平均"""
    result = []
    for i in range(len(data)):
        if i < window_size - 1:
            # 不足窗口大小时，取已有的数据平均值
            window = data[:i+1]
        else:
            window = data[i-window_size+1:i+1]
        result.append(sum(window) / len(window))
    return np.array(result)

# 使用NumPy优化的函数
def calculate_moving_average_numpy(data, window_size):
    """使用NumPy计算移动平均"""
    # 使用卷积方法
    weights = np.ones(window_size) / window_size
    # 卷积计算
    result = np.convolve(data, weights, mode='full')
    # 调整结果长度与输入相同
    return result[:len(data)]

# 使用Numba JIT优化的函数
@njit(parallel=False)
def calculate_moving_average_numba(data, window_size):
    """使用Numba JIT优化计算移动平均"""
    result = np.zeros_like(data)
    for i in range(len(data)):
        window_start = max(0, i - window_size + 1)
        window = data[window_start:i+1]
        result[i] = np.mean(window)
    return result

# 使用Numba并行优化的函数
@njit(parallel=True)
def calculate_moving_average_numba_parallel(data, window_size):
    """使用Numba并行计算移动平均"""
    result = np.zeros_like(data)
    # 使用prange进行并行循环
    for i in prange(len(data)):
        window_start = max(0, i - window_size + 1)
        window = data[window_start:i+1]
        # 手动计算平均值以避免并行中的一些问题
        window_sum = 0.0
        for j in range(window.size):
            window_sum += window[j]
        result[i] = window_sum / window.size
    return result

# 性能测试
window_size = 50

# 预热Numba函数（JIT编译）
_ = calculate_moving_average_numba(np.random.rand(100), 10)
_ = calculate_moving_average_numba_parallel(np.random.rand(100), 10)

# 测试Python版本
start_time = time.time()
python_result = calculate_moving_average_python(data[:10000], window_size)
python_time = time.time() - start_time
print(f"Python版本耗时: {python_time:.6f} 秒 (仅测试10000个数据点)")

# 测试NumPy版本
start_time = time.time()
numpy_result = calculate_moving_average_numpy(data, window_size)
numpy_time = time.time() - start_time
print(f"NumPy版本耗时: {numpy_time:.6f} 秒")

# 测试Numba版本
start_time = time.time()
numba_result = calculate_moving_average_numba(data, window_size)
numba_time = time.time() - start_time
print(f"Numba版本耗时: {numba_time:.6f} 秒")

# 测试Numba并行版本
start_time = time.time()
numba_parallel_result = calculate_moving_average_numba_parallel(data, window_size)
numba_parallel_time = time.time() - start_time
print(f"Numba并行版本耗时: {numba_parallel_time:.6f} 秒")

# 验证结果正确性
print(f"\n结果验证:")
print(f"NumPy与Numba结果是否一致: {np.allclose(numpy_result, numba_result)}")
print(f"NumPy与Numba并行结果是否一致: {np.allclose(numpy_result, numba_parallel_result)}")

# 异常检测算法在边缘设备上的实现

# 1. Z-Score异常检测
@njit
def zscore_detection(data, threshold=3.0):
    """使用Z-Score方法检测异常值"""
    # 计算均值和标准差
    mean_val = np.mean(data)
    std_val = np.std(data)
    
    # 避免除以零
    if std_val == 0:
        return np.zeros_like(data, dtype=np.bool_)
    
    # 计算Z-Score
    z_scores = np.abs((data - mean_val) / std_val)
    
    # 标记异常值
    return z_scores > threshold

# 2. 移动平均异常检测
@njit
def moving_average_detection(data, window_size=50, threshold=2.0):
    """使用移动平均和移动标准差检测异常"""
    n = len(data)
    is_anomaly = np.zeros(n, dtype=np.bool_)
    
    # 预先计算移动均值和移动标准差
    for i in range(n):
        window_start = max(0, i - window_size + 1)
        window = data[window_start:i+1]
        
        if len(window) < 10:  # 至少需要10个数据点
            continue
        
        mean_val = np.mean(window)
        std_val = np.std(window)
        
        if std_val > 0:  # 避免除以零
            # 计算当前值与移动均值的偏差
            deviation = abs(data[i] - mean_val) / std_val
            is_anomaly[i] = deviation > threshold
    
    return is_anomaly

# 3. IQR（四分位距）异常检测
@njit
def iqr_detection(data, threshold=1.5):
    """使用IQR方法检测异常值"""
    # 计算四分位数
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    
    # 计算上下边界
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    
    # 标记异常值
    return (data < lower_bound) | (data > upper_bound)

# 测试异常检测算法
# 生成测试数据（包含一些异常值）
def generate_test_data(size=1000, anomaly_count=5):
    # 正常数据（高斯分布）
    data = np.random.normal(loc=25, scale=2, size=size)
    
    # 添加异常值
    anomaly_indices = np.random.choice(size, anomaly_count, replace=False)
    for idx in anomaly_indices:
        # 随机选择是添加极高值还是极低值
        if np.random.random() > 0.5:
            data[idx] = data[idx] + np.random.uniform(10, 20)
        else:
            data[idx] = data[idx] - np.random.uniform(10, 20)
    
    return data, anomaly_indices

# 生成测试数据
test_data, true_anomalies = generate_test_data()

# 运行异常检测
zscore_anomalies = zscore_detection(test_data)
moving_avg_anomalies = moving_average_detection(test_data)
iqr_anomalies = iqr_detection(test_data)

# 评估检测性能
def evaluate_detection(true_indices, detected):
    """评估异常检测算法性能"""
    # 计算真阳性、假阳性、假阴性
    true_positive = 0
    false_positive = 0
    false_negative = 0
    
    # 创建真实异常值的集合
    true_set = set(true_indices)
    
    # 遍历检测结果
    for i in range(len(detected)):
        if detected[i]:
            if i in true_set:
                true_positive += 1
            else:
                false_positive += 1
        elif i in true_set:
            false_negative += 1
    
    # 计算准确率、召回率和F1分数
    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return {
        "true_positive": true_positive,
        "false_positive": false_positive,
        "false_negative": false_negative,
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score
    }

# 评估算法
zscore_metrics = evaluate_detection(true_anomalies, zscore_anomalies)
moving_avg_metrics = evaluate_detection(true_anomalies, moving_avg_anomalies)
iqr_metrics = evaluate_detection(true_anomalies, iqr_anomalies)

print("\n异常检测算法评估:")
print("Z-Score 方法:")
print(json.dumps(zscore_metrics, indent=2))
print("\n移动平均方法:")
print(json.dumps(moving_avg_metrics, indent=2))
print("\nIQR 方法:")
print(json.dumps(iqr_metrics, indent=2))

# 使用Redis进行边缘设备数据缓存和共享

# 安装: pip install redis

import redis

class EdgeDataCache:
    def __init__(self, host='localhost', port=6379, db=0):
        """初始化Redis连接"""
        try:
            self.redis_client = redis.Redis(host=host, port=port, db=db)
            # 测试连接
            self.redis_client.ping()
            print(f"已连接到Redis服务器: {host}:{port}")
            self.connected = True
        except redis.ConnectionError:
            print(f"无法连接到Redis服务器: {host}:{port}")
            print("将使用内存缓存作为备选")
            self.redis_client = None
            self.connected = False
            # 使用Python字典作为内存缓存
            self.memory_cache = {}
    
    def store_sensor_data(self, device_id, sensor_type, data, expire_seconds=3600):
        """存储传感器数据"""
        key = f"sensor:{device_id}:{sensor_type}"
        
        # 将数据序列化为JSON
        json_data = json.dumps(data)
        
        if self.connected:
            try:
                # 存储数据并设置过期时间
                self.redis_client.setex(key, expire_seconds, json_data)
                return True
            except Exception as e:
                print(f"Redis存储错误: {e}")
                # 回退到内存缓存
                self.memory_cache[key] = (json_data, time.time() + expire_seconds)
                return True
        else:
            # 使用内存缓存
            self.memory_cache[key] = (json_data, time.time() + expire_seconds)
            return True
    
    def get_sensor_data(self, device_id, sensor_type):
        """获取传感器数据"""
        key = f"sensor:{device_id}:{sensor_type}"
        
        if self.connected:
            try:
                # 从Redis获取数据
                data = self.redis_client.get(key)
                if data:
                    return json.loads(data)
                return None
            except Exception as e:
                print(f"Redis读取错误: {e}")
                # 回退到内存缓存
                return self._get_from_memory_cache(key)
        else:
            # 从内存缓存获取
            return self._get_from_memory_cache(key)
    
    def _get_from_memory_cache(self, key):
        """从内存缓存获取数据"""
        if key in self.memory_cache:
            data, expire_time = self.memory_cache[key]
            # 检查是否过期
            if time.time() < expire_time:
                return json.loads(data)
            else:
                # 删除过期数据
                del self.memory_cache[key]
        return None
    
    def store_time_series_data(self, device_id, metric, timestamp, value):
        """存储时间序列数据"""
        key = f"timeseries:{device_id}:{metric}"
        
        if self.connected:
            try:
                # 使用Redis的有序集合存储时间序列
                self.redis_client.zadd(key, {json.dumps({"value": value}): timestamp})
                # 保留最近1000个数据点
                self.redis_client.zremrangebyrank(key, 0, -1001)
                return True
            except Exception as e:
                print(f"Redis时间序列存储错误: {e}")
                return False
        else:
            # 简化的内存存储（仅保存最新值）
            mem_key = f"{key}:latest"
            self.memory_cache[mem_key] = (json.dumps({"timestamp": timestamp, "value": value}), float('inf'))
            return True
    
    def get_time_series_data(self, device_id, metric, start_time=None, end_time=None, limit=100):
        """获取时间序列数据"""
        key = f"timeseries:{device_id}:{metric}"
        
        if self.connected:
            try:
                # 设置范围
                min_score = start_time if start_time else -
                max_score = end_time if end_time else +
                
                # 获取数据
                data = self.redis_client.zrangebyscore(key, min_score, max_score, withscores=True, start=0, num=limit)
                
                # 解析结果
                result = []
                for value_data, timestamp in data:
                    value_dict = json.loads(value_data)
                    result.append({
                        "timestamp": timestamp,
                        "value": value_dict["value"]
                    })
                
                return result
            except Exception as e:
                print(f"Redis时间序列读取错误: {e}")
                # 尝试返回最新值
                mem_key = f"{key}:latest"
                latest_data = self._get_from_memory_cache(mem_key)
                return [latest_data] if latest_data else []
        else:
            # 返回内存中的最新值
            mem_key = f"{key}:latest"
            latest_data = self._get_from_memory_cache(mem_key)
            return [latest_data] if latest_data else []
    
    def clear_device_data(self, device_id):
        """清除特定设备的所有数据"""
        if self.connected:
            try:
                # 获取所有相关键
                pattern = f"*:{device_id}:*"
                keys = self.redis_client.keys(pattern)
                if keys:
                    self.redis_client.delete(*keys)
                return True
            except Exception as e:
                print(f"Redis清除错误: {e}")
                return False
        else:
            # 清理内存缓存
            keys_to_delete = []
            for key in self.memory_cache:
                if f":{device_id}:" in key:
                    keys_to_delete.append(key)
            
            for key in keys_to_delete:
                del self.memory_cache[key]
            
            return True

# 使用示例
# cache = EdgeDataCache()
# 
# # 存储传感器数据
# sensor_data = {
#     "value": 26.5,
#     "timestamp": time.time(),
#     "unit": "°C"
# }
# cache.store_sensor_data("device_01", "temperature", sensor_data)
# 
# # 获取传感器数据
# retrieved_data = cache.get_sensor_data("device_01", "temperature")
# print(f"\n检索到的数据: {retrieved_data}")
# 
# # 存储时间序列数据
# for i in range(10):
#     timestamp = time.time() - (10 - i) * 60  # 过去10分钟的数据，每分钟一个点
#     value = 25 + i * 0.5  # 从25度开始，每分钟增加0.5度
#     cache.store_time_series_data("device_01", "temperature", timestamp, value)
# 
# # 获取时间序列数据
# time_series_data = cache.get_time_series_data("device_01", "temperature", limit=5)
# print(f"\n获取的时间序列数据:")
# for point in time_series_data:
#     print(f"  时间: {point['timestamp']}, 值: {point['value']}")
```

## 3. 低代码与无代码开发

### 3.1 Python低代码平台与框架
**[标识: LOWCODE-FRAMEWORK-001]**

Python驱动的低代码开发平台和框架的使用指南。

```python
# 使用Streamlit快速构建Web应用

# 安装: pip install streamlit pandas matplotlib plotly

"""
使用方法：
1. 将以下代码保存为 app.py
2. 运行: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# 设置页面配置
st.set_page_config(
    page_title="数据可视化仪表板",
    page_icon="📊",
    layout="wide"
)

# 页面标题
st.title("交互式数据可视化仪表板")

# 侧边栏
with st.sidebar:
    st.header("设置")
    
    # 选择数据源
    data_source = st.radio(
        "选择数据源",
        ("使用示例数据", "上传CSV文件")
    )
    
    # 上传文件选项
    uploaded_file = None
    if data_source == "上传CSV文件":
        uploaded_file = st.file_uploader("上传CSV文件", type="csv")
    
    # 图表类型选择
    chart_type = st.selectbox(
        "选择图表类型",
        ("折线图", "柱状图", "散点图", "热力图", "箱线图")
    )
    
    # 颜色主题
    theme = st.select_slider(
        "选择颜色主题",
        options=["默认", "明亮", "暗色", "彩色"]
    )

# 生成或加载数据
if data_source == "使用示例数据":
    # 生成示例数据
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
    
    # 创建一个包含多个指标的DataFrame
    data = pd.DataFrame({
        "日期": dates,
        "销售额": np.random.normal(1000, 200, len(dates)),
        "访问量": np.random.normal(5000, 1000, len(dates)),
        "转化率": np.random.normal(0.05, 0.01, len(dates)),
        "客单价": np.random.normal(200, 50, len(dates))
    })
    
    # 添加一些分类数据
    categories = ["电子产品", "服装", "食品", "家居", "书籍"]
    data["类别"] = np.random.choice(categories, size=len(dates))
    
    st.info("使用了示例销售数据")
else:
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            st.success("文件上传成功！")
            
            # 显示数据预览
            st.subheader("数据预览")
            st.dataframe(data.head())
        except Exception as e:
            st.error(f"文件读取错误: {e}")
            st.stop()
    else:
        st.warning("请上传CSV文件")
        st.stop()

# 数据处理区域
st.subheader("数据统计信息")

# 显示基本统计信息
col1, col2 = st.columns(2)
with col1:
    st.write("数据维度:")
    st.info(f"行数: {data.shape[0]}, 列数: {data.shape[1]}")
    
with col2:
    st.write("数值列统计:")
    st.dataframe(data.describe())

# 交互式数据选择器
st.subheader("数据筛选")

# 为数值列创建筛选器
numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
selected_cols = st.multiselect(
    "选择要分析的数值列",
    options=numeric_cols,
    default=numeric_cols[:2] if numeric_cols else []
)

# 为分类列创建筛选器
cat_cols = data.select_dtypes(include=['object', 'category']).columns.tolist()
if cat_cols:
    selected_cat_col = st.selectbox(
        "选择分类列",
        options=cat_cols
    )
    
    if selected_cat_col:
        unique_cats = data[selected_cat_col].unique()
        selected_cats = st.multiselect(
            f"选择{selected_cat_col}的类别",
            options=unique_cats,
            default=list(unique_cats[:3]) if len(unique_cats) > 3 else list(unique_cats)
        )
        
        # 应用分类筛选
        if selected_cats:
            data = data[data[selected_cat_col].isin(selected_cats)]

# 绘制图表
st.subheader("数据可视化")

# 检查是否有日期列用于时间序列
if any(data.columns.str.contains('日期|date|time', case=False)):
    date_col = [col for col in data.columns if any(x in col.lower() for x in ['日期', 'date', 'time'])][0]
    data[date_col] = pd.to_datetime(data[date_col])
    
    # 时间范围选择
    min_date = data[date_col].min().date()
    max_date = data[date_col].max().date()
    
    start_date, end_date = st.date_input(
        "选择日期范围",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # 应用日期筛选
    data = data[(data[date_col].dt.date >= start_date) & (data[date_col].dt.date <= end_date)]

# 根据选择的图表类型进行可视化
if selected_cols and not data.empty:
    if chart_type == "折线图":
        fig = go.Figure()
        for col in selected_cols:
            fig.add_trace(go.Scatter(
                x=data[date_col] if 'date_col' in locals() else data.index,
                y=data[col],
                mode='lines',
                name=col
            ))
        
        fig.update_layout(
            title="时间序列折线图",
            xaxis_title="日期",
            yaxis_title="值",
            legend_title="指标"
        )
        
    elif chart_type == "柱状图":
        # 按类别分组统计
        if 'selected_cat_col' in locals() and selected_cat_col:
            grouped_data = data.groupby(selected_cat_col)[selected_cols].mean().reset_index()
            fig = px.bar(
                grouped_data,
                x=selected_cat_col,
                y=selected_cols,
                barmode='group',
                title=f"按{selected_cat_col}分组的柱状图"
            )
        else:
            # 简单柱状图
            fig = go.Figure()
            for col in selected_cols:
                fig.add_trace(go.Bar(
                    x=data.index[:50],  # 只显示前50个数据点
                    y=data[col][:50],
                    name=col
                ))
            fig.update_layout(title="柱状图", xaxis_title="索引", yaxis_title="值")
    
    elif chart_type == "散点图":
        if len(selected_cols) >= 2:
            fig = px.scatter(
                data,
                x=selected_cols[0],
                y=selected_cols[1],
                color=selected_cat_col if 'selected_cat_col' in locals() and selected_cat_col else None,
                size=selected_cols[2] if len(selected_cols) > 2 else None,
                hover_data=data.columns,
                title="散点图"
            )
        else:
            st.warning("散点图需要至少两列数据")
            st.stop()
    
    elif chart_type == "热力图":
        # 计算相关系数矩阵
        corr_matrix = data[selected_cols].corr()
        fig = px.imshow(
            corr_matrix,
            text_auto=True,
            aspect="auto",
            title="相关性热力图"
        )
    
    elif chart_type == "箱线图":
        fig = go.Figure()
        for col in selected_cols:
            fig.add_trace(go.Box(
                y=data[col],
                name=col,
                boxpoints='all'
            ))
        fig.update_layout(title="箱线图", yaxis_title="值")
    
    # 设置主题
    if theme == "暗色":
        fig.update_layout(template="plotly_dark")
    elif theme == "明亮":
        fig.update_layout(template="plotly_white")
    elif theme == "彩色":
        fig.update_layout(template="plotly_express_colorway")
    
    # 显示图表
    st.plotly_chart(fig, use_container_width=True)
    
    # 提供下载选项
    st.download_button(
        label="下载图表为PNG",
        data=fig.to_image(format="png"),
        file_name="chart.png",
        mime="image/png"
    )
else:
    st.warning("请选择要分析的列或上传有效数据")

# 数据导出区域
st.subheader("数据导出")

# 提供数据导出选项
if st.button("导出筛选后的数据为CSV"):
    csv = data.to_csv(index=False)
    st.download_button(
        label="下载CSV文件",
        data=csv,
        file_name="filtered_data.csv",
        mime="text/csv"
    )

# 使用Dash构建交互式Web应用

"""
# 安装: pip install dash dash-bootstrap-components pandas plotly

from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px

# 生成示例数据
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
data = pd.DataFrame({
    "日期": dates,
    "销售额": np.random.normal(1000, 200, len(dates)),
    "访问量": np.random.normal(5000, 1000, len(dates)),
    "转化率": np.random.normal(0.05, 0.01, len(dates)),
    "客单价": np.random.normal(200, 50, len(dates)),
    "类别": np.random.choice(["电子产品", "服装", "食品", "家居", "书籍"], size=len(dates))
})

# 创建Dash应用
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 应用布局
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("交互式数据分析仪表板"), className="mb-4 mt-4")
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H5("设置"),
            html.Label("选择指标"),
            dcc.Dropdown(
                id='metric-dropdown',
                options=[
                    {'label': '销售额', 'value': '销售额'},
                    {'label': '访问量', 'value': '访问量'},
                    {'label': '转化率', 'value': '转化率'},
                    {'label': '客单价', 'value': '客单价'}
                ],
                value='销售额',
                clearable=False
            ),
            
            html.Label("选择类别", className="mt-3"),
            dcc.Checklist(
                id='category-checklist',
                options=[
                    {'label': '电子产品', 'value': '电子产品'},
                    {'label': '服装', 'value': '服装'},
                    {'label': '食品', 'value': '食品'},
                    {'label': '家居', 'value': '家居'},
                    {'label': '书籍', 'value': '书籍'}
                ],
                value=["电子产品", "服装", "食品"],
                inline=True
            ),
            
            html.Label("选择时间范围", className="mt-3"),
            dcc.DatePickerRange(
                id='date-range',
                start_date=data["日期"].min(),
                end_date=data["日期"].max(),
                display_format='YYYY-MM-DD'
            )
        ], width=3),
        
        dbc.Col([
            dcc.Graph(id='time-series-chart')
        ], width=9)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='distribution-chart')
        ], width=6),
        
        dbc.Col([
            dcc.Graph(id='category-chart')
        ], width=6)
    ], className="mt-4")
], fluid=True)

# 回调函数 - 更新时间序列图表
@app.callback(
    Output('time-series-chart', 'figure'),
    [Input('metric-dropdown', 'value'),
     Input('category-checklist', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_time_series(selected_metric, selected_categories, start_date, end_date):
    # 筛选数据
    filtered_data = data[
        (data['类别'].isin(selected_categories)) &
        (data['日期'] >= start_date) &
       