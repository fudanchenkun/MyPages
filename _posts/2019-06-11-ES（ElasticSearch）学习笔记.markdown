# ES elasticsearch

## 索引架构
### index和shard

> index -> type -> mapping -> document -> field

![image](872B9F4C235744A681D04DEBA4AFC889)

定义好数据存储的在index上，每个index的数据会分布在多个shard上，每个shard会有备份。主shard称为primary shard，备份的shard称为replica shard。primary shard宕机时，会自动选出replica shard。

每个shard其实是一个Lucene索引，分布数据的过程就是**分片**处理即sharding

![image](FB5225B5BAB6437BAB587C190C264441)

![image](C618B02222A54FF5B9A980840B179A31)


### 游标会话
```python
from elasticsearch.helpers import scan as _scan
_scan(
            self.client,
            index=self.index_name,
            query=_json.loads(content),
            size=1000,
            request_timeout=cur_timeout,
            timeout='%ds' % (cur_timeout + 1),
            scroll="1m"
        )
```

### 高负载的场景下使用ES
- 索引刷新频率：文档需要多久才能出现在搜索结果中。刷新频率越短，查询越慢，吞吐量越低。
- 增加线程数和队列长度
- 调整合并过程 Lucene段合并调整？es会限制
- 将索引分散到多个分片上来降低单个服务器的负载。

## 目录实现-store模块
1. simplefs 随机存取文件 64位 win系统
2. niofs 基于java NIO的实现 64位 Unix系统
3. mmap 读文件时，会将文件映射到同样大小的虚拟地址空间去。等价于允许Lucene或es之间访问IO缓存，只限于32位系统。
4. default 混合使用NIO和mmap
5. memory 内存store类型 不可持久化

## 底层索引控制
在mapping中设置每个字段的相似度模型，使用关键字similarity


### es中的索引可能由一个或者多个Lucene索引构成？

es中的字段包含一个或多个字段值，不用写成list

### es包含哪些类型的节点？
1. data node 用于索引数据
2. master node 监督和控制其他节点
3. 部落节点 tribe node 连接多个集群



### 副本的作用？
1、分担节点查询的负载
2、容错，防止某节点宕机

### discovery模块的作用？
用于发现的新的节点，es是对等架构，主节点是自动推选出来的，分发索引到集群的相应节点。

### 怎么进行故障检测？
主节点会监控所有节点，某个节点在一定时间内未能响应，则断开，进行故障处理，可能会对集群分片重新负载均衡。如果主分片故障，那么就会从副分片推选出主分片。
主节点通过ping来发现故障节点，同时数据节点也会通过ping来判断主节点是否有故障。

### es的通信？
基于rest、http协议，java API提供了所有可能被rest API调用的功能
- 如何索引API有哪几种方式？
1. 就是通过url，向对应的节点（9200端口）发送json数据，基于http协议
2. 通过bulk API或者UDP bulk API（基于UDP协议），批量发送多个文档到集群。
其中，创建操作只会发生在主节点上，如果该节点没有主节点，该节点就会转发该数据，然后由主节点来群发给副本。
- 查询过程？
   + 分散阶段（scatter phase）：将查询分发到包含该文档的多个分片中查询
   + 合并阶段（gather phase）：将查询结果收集，然后合并、排序

### Lucene评分公式
TF/IDF (Term Frequency , inverse document frequency)
该词在文档中的出现频率，该词在所有文档中出现的频率

### 查询过滤的区别
过滤是指“post_filter”关键字，过滤的唯一作用是缩小范围，但不影响评分，而查询会影响评分

### 过滤器
- 一般时使用了Bits的过滤器效率高（cpu通过位运算），如bool过滤器，而与或非过滤器不用。
- 一般区间、脚本、geo的过滤器不使用Bits，这些过滤器的组合是个漏斗，可以把匹配文档多的过滤器放在最前面，提高性能。

### 设置分片和副本
```JSON
“index”:{
"number_of_shards":1,
"number_of_replicas": 0
}
```

### 路由
- 指定哪些数据存到哪些分片中，也指定在哪个分区上查询
- 路由确保了在索引时拥有相同又幼稚的文档被索引到了相同的分片上
- 但同一个分片上可能拥有不同路由值的文档。
```
curl -XPUT localhost:9200/books/doc/1?routing=A -d '{"name": "xxxx"}'
```


### 删除所有doc
```
curl -XDELETE 'localhost:9200/document/_query?q=*:*'
```

### 部署意识
分配几个node.group值，如groupA、groupB，那么主分片和副本就不会同时存储在groupA或者同时 存在groupB中。




