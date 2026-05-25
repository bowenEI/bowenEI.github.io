---
# Documentation: https://hugoblox.com/docs/managing-content/

title: "基本概念"
linktitle: "基本概念"
date: 2024-03-20T01:49:51+08:00
type: docs
summary: ""
weight: 10
---

## 文档（Document）

MongoDB 的核心数据单元，类似于 JSON 对象，采用 **BSON**（Binary JSON）格式存储。

```json
{
  "_id": ObjectId("..."),
  "name": "Alice",
  "age": 30,
  "email": "alice@example.com",
  "address": {
    "city": "Beijing",
    "zip": "100000"
  },
  "tags": ["developer", "python"],
  "created_at": ISODate("2026-01-01T00:00:00Z")
}
```

**字段类型**：

| 类型          | 说明         | 示例                                      |
| ------------- | ------------ | ----------------------------------------- |
| `String`      | UTF-8 字符串 | `"hello"`                                 |
| `Integer`     | 32/64 位整数 | `42`, `NumberLong("9223372036854775807")` |
| `Double`      | 64 位浮点    | `3.14159`                                 |
| `Boolean`     | 布尔值       | `true`, `false`                           |
| `Array`       | 数组         | `["a", "b", "c"]`                         |
| `Object`      | 嵌套文档     | `{"key": "value"}`                        |
| `Null`        | 空值         | `null`                                    |
| `Date`        | UTC 日期时间 | `ISODate("2026-01-01")`                   |
| `ObjectId`    | 文档唯一 ID  | `ObjectId("...")`                         |
| `Binary Data` | 二进制数据   | 二进制字节串                              |
| `Regex`       | 正则表达式   | `/^test/i`                                |

**ObjectId 结构**（12 字节）：

```
┌──────────┬──────────┬──────────┬──────────┐
│ 时间戳(4)│ 机器ID(3)│ 进程ID(2)│ 计数器(3)│
└──────────┴──────────┴──────────┴──────────┘
```

## 集合（Collection）

一组文档的容器，类似于关系型数据库的表，但**无固定Schema**（模式自由）。

**集合命名规范**：

- 不能以 `system.` 开头（系统保留）
- 不能包含 `$`
- 不能包含空字符串
- 建议使用复数形式：`users`, `products`, `orders`

## 数据库（Database）

集合的逻辑容器，一个 MongoDB 实例可包含多个数据库。

```bash
# 保留数据库
admin     # 用于管理员操作
local     # 用于本地复制
config    # 用于分片配置
```

## 命名空间（Namespace）

`数据库.集合` 构成完整命名空间，例如 `mydb.users`。

## 核心特性

| 特性          | 说明                                       |
| ------------- | ------------------------------------------ |
| **无 Schema** | 同一集合的文档字段可以不同                 |
| **水平扩展**  | 通过分片支持海量数据                       |
| **高可用**    | 副本集（Replica Set）提供自动故障转移      |
| **灵活查询**  | 强大的文档查询语言，支持嵌套查询           |
| **索引**      | 支持单字段、复合、多键、文本、地理空间索引 |
| **聚合框架**  | 处理流水线式的文档转换                     |

## 系统架构

```mermaid
flowchart TD
  A[Application Layer<br/>MongoDB Drivers / Shell] --> B[mongos Router<br/>Query Routing / Sharding]
  B --> C[Shard 1<br/>副本集]
  B --> D[Shard 2<br/>副本集]
  B --> E[Shard 3<br/>副本集]
```

## 安装与连接

```bash
# Docker 快速启动
docker run -d --name mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password \
  mongo:latest

# 连接
mongosh "mongodb://admin:password@localhost:27017"
# 或
mongo "mongodb://admin:password@localhost:27017"
```
