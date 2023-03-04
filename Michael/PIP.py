import speedtest
test = speedtest.Speedtest();
down = test.download();
up = test.upload();
print(f'Taxa de Download: {down:.2f}')
print(f'Tava de Upload: {up:.2f}')