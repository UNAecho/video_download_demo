#!/usr/bin/env python3
"""
WireGuard配置文件批量生成器
"""

import os

def generate_config_file(config, output_path, endpoint_ip):
    """生成WireGuard配置文件"""
    lines = [
        '[Interface]',
        f"PrivateKey = {config['PrivateKey']}",
        f"Address = {config['Address']}",
        f"DNS = {config['DNS']}",
        '',
        '[Peer]',
        f"PublicKey = {config['PublicKey']}",
        f"AllowedIPs = {config['AllowedIPs']}",
        f"Endpoint = {endpoint_ip}"
    ]

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def main():
    # WireGuard配置参数
    wireguard_config = {
        'PrivateKey': 'your_private_key_placeholder',
        'Address': '10.14.0.2/16',
        'DNS': '8.8.8.8, 8.8.4.4',
        'PublicKey': 'your_public_key_placeholder',
        'AllowedIPs': '0.0.0.0/0'
    }

    # 生成设置
    settings = {
        'output_dir': 'wireguard_configs',
        'file_prefix': 'wireguard_config',
        'ip_base': '192.168.1.1',
        'start_ip': 1,
        'end_ip': 3,
        'port': '51820'
    }

    # 创建输出目录
    if not os.path.exists(settings['output_dir']):
        os.makedirs(settings['output_dir'])

    # 批量生成配置文件
    for i in range(settings['start_ip'], settings['end_ip'] + 1):
        endpoint_ip = f"{settings['ip_base']}.{i}:{settings['port']}"
        filename = f"{settings['file_prefix']}-{i}.conf"
        output_path = os.path.join(settings['output_dir'], filename)

        generate_config_file(wireguard_config, output_path, endpoint_ip)
        print(f"生成文件: {filename} -> {endpoint_ip}")

    print(f"\n生成完成! 共 {settings['end_ip'] - settings['start_ip'] + 1} 个配置文件")

if __name__ == "__main__":
    main()