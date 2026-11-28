# 字符 ↔ 十六进制双向转换器（char-hex-converter）

> 支持字符转十六进制、十六进制转字符的双向转换器。A bidirectional converter between characters and hexadecimal.
> 
> [main.py](src/main.py)  脚本在Windows环境中运行、测试，适配 [python-3.10](https://www.python.org/ftp/python/3.10.0/python-3.10.0rc2-amd64.exe) 程序。

## 打包命令示例

> 在Windows Powershell终端打包，打包结果放在pack子文件夹

``` bash
python -m PyInstaller --noconfirm --clean --onefile --windowed `
  --name "十六进制转换器" `
  --distpath pack --workpath "pack\build" --specpath pack `
  "src\main.py"
```

## notepad++ 运行python脚本
```bash
cmd /k cd /d "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" & echo. & pause & exit
```

## 代码推送与镜像同步说明

本项目的代码推送流程如下：

```text
本地代码 → AtomGit → 自动镜像同步 → 腾讯云 CNB / GitHub / Gitee
```

## 你可以在这些地方找到我 (Find Me Here)

<p align="center">
  <a href="https://gitcode.com/techtest/char-hex-converter.git" target="_blank" rel="noopener">
    <img src="images/6e5e33151cf7d4b69bc75e984af332d9.png" width="18" height="18" alt="GitCode">&nbsp;GitCode
  </a>
  <span style="color: #999;">&nbsp;/&nbsp;</span>
  <a href="https://atomgit.com/techtest/char-hex-converter.git" target="_blank" rel="noopener">&nbsp;AtomGit
  </a>
  &nbsp;&nbsp;
  <a href="https://cnb.cool/iaoexl/techtest/char-hex-converter.git" target="_blank" rel="noopener">
    <img src="images/204dc4444f152572ee9977c2ee15b1e4.png" width="18" height="18" alt="腾讯云 CNB">&nbsp;腾讯云 CNB
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/iaoexl/char-hex-converter.git" target="_blank" rel="noopener">
    <img src="images/c31718c62908f5248d95dff0fe0c96f7.png" width="18" height="18" alt="GitHub">&nbsp;GitHub
  </a>
  &nbsp;&nbsp;
  <a href="https://gitee.com/techtest/char-hex-converter.git" target="_blank" rel="noopener">
    <img src="images/2765d9743c9a0ddfdf7a9bd9df4cab82.png" width="18" height="18" alt="Gitee">&nbsp;Gitee
  </a>
</p>

<!--
## 支持这个项目（Support This Project）

如果这个项目对你有帮助，欢迎[赞助支持](SPONSOR.md)。
-->