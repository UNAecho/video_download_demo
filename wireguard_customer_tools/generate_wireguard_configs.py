#!/usr/bin/env python3
"""
WireGuard配置文件生成器
"""

import os

def read_wireguard_config(file_path):
    """读取WireGuard配置文件，解析key-value"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    config = {
        'Interface': {},
        'Peer': {}
    }
    current_section = None

    for line in content.split('\n'):
        line = line.strip()

        if not line or line.startswith('#'):
            continue

        if line == '[Interface]':
            current_section = 'Interface'
        elif line == '[Peer]':
            current_section = 'Peer'
        elif '=' in line and current_section:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            config[current_section][key] = value

    return config

def generate_config_file(template_config, replacements, output_path, endpoint_ip):
    """根据模板配置和替换规则生成新的配置文件"""
    lines = []
    lines.append('[Interface]')

    # 替换Interface部分的配置
    for key, value in template_config['Interface'].items():
        if key in replacements['Interface']:
            new_value = replacements['Interface'][key]
        else:
            new_value = value
        lines.append(f"{key} = {new_value}")

    lines.append('')
    lines.append('[Peer]')

    # 替换Peer部分的配置
    for key, value in template_config['Peer'].items():
        if key in replacements['Peer']:
            if key == 'Endpoint':
                new_value = endpoint_ip
            else:
                new_value = replacements['Peer'][key]
        else:
            new_value = value
        lines.append(f"{key} = {new_value}")

    # 写入新配置文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def main():
    # 配置参数
    settings = {
        'template_file': 'wireguard_config.conf',
        'output_dir': 'wireguard_configs',
        'file_prefix': 'wireguard_config',
        'ip_base': '192.168.1.1',
        'start_ip': 1,
        'end_ip': 3,
        'port': '51820',
        'replacements': {
            'Interface': {
                'PrivateKey': 'your_private_key_placeholder',
                'DNS': '8.8.8.8, 8.8.4.4',
            },
            'Peer': {
                'PublicKey': 'your_public_key_placeholder',
                'AllowedIPs': '0.0.0.0/0',
            }
        }
    }

    # 检查模板文件
    if not os.path.exists(settings['template_file']):
        print(f"找不到配置文件: {settings['template_file']}")
        return

    # 创建输出目录
    if not os.path.exists(settings['output_dir']):
        os.makedirs(settings['output_dir'])

    # 读取模板配置
    template_config = read_wireguard_config(settings['template_file'])

    # 生成配置文件
    for i in range(settings['start_ip'], settings['end_ip'] + 1):
        endpoint_ip = f"{settings['ip_base']}.{i}:{settings['port']}"
        filename = f"{settings['file_prefix']}-{i}.conf"
        output_path = os.path.join(settings['output_dir'], filename)

        generate_config_file(template_config, settings['replacements'], output_path, endpoint_ip)
        print(f"生成文件: {filename} -> {endpoint_ip}")

    print(f"\n生成完成! 共 {settings['end_ip'] - settings['start_ip'] + 1} 个配置文件")

if __name__ == "__main__":
    main()