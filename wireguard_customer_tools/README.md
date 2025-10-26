# WireGuard配置文件批量生成器

由于一些VPN公司给予的WireGuard配置文件，每天的IP都在变，写了一个自动生成对应范围WireGuard配置文件的工具

## 使用方法
```bash
python generate_wireguard_configs.py
```

## 配置说明
修改脚本中的`settings`配置项来指定模板文件、IP范围、密钥等参数。