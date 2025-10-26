#!/usr/bin/env python3
"""
WireGuard配置文件批量生成器
"""

import os

def generate_config_file(config, output_path, endpoint_ip):
    """生成WireGuard配置文件"""
    lines = [
        '[Interface]',
        f"PrivateKey = {config['Interface']['PrivateKey']}",
        f"Address = {config['Interface']['Address']}",
        f"DNS = {config['Interface']['DNS']}",
        '',
        '[Peer]',
        f"PublicKey = {config['Peer']['PublicKey']}",
        f"AllowedIPs = {config['Peer']['AllowedIPs']}",
        f"Endpoint = {endpoint_ip}"
    ]

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def main():
    # 配置参数
    config = {
        # Interface配置
        'Interface': {
            'PrivateKey': 'your_private_key_placeholder',
            'Address': '10.14.0.2/16',
            'DNS': '8.8.8.8, 8.8.4.4'
        },

        # Peer配置
        'Peer': {
            'PublicKey': 'your_public_key_placeholder',
            'AllowedIPs': '0.0.0.0/0',
            'endpoint_base': '192.168.1.1',
            'port': '51820',
            'start_ip': 1,
            'end_ip': 3
        },

        # 生成设置
        'output_dir': 'wireguard_configs',
        'file_prefix': 'wireguard_config'
    }

    # 创建输出目录
    if not os.path.exists(config['output_dir']):
        os.makedirs(config['output_dir'])

    # 批量生成配置文件
    for i in range(config['Peer']['start_ip'], config['Peer']['end_ip'] + 1):
        endpoint_ip = f"{config['Peer']['endpoint_base']}.{i}:{config['Peer']['port']}"
        filename = f"{config['file_prefix']}-{i}.conf"
        output_path = os.path.join(config['output_dir'], filename)

        generate_config_file(config, output_path, endpoint_ip)
        print(f"生成文件: {filename} -> {endpoint_ip}")

    print(f"\n生成完成! 共 {config['Peer']['end_ip'] - config['Peer']['start_ip'] + 1} 个配置文件")

if __name__ == "__main__":
    main()