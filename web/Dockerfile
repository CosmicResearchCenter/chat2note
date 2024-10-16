# 使用 node 作为基础镜像来构建项目
FROM node:16-alpine as build

# 设置工作目录
WORKDIR /app

# 复制 package.json 和 package-lock.json 并安装依赖
COPY package*.json ./
RUN npm install

# 复制项目的源代码
COPY . .

# 构建项目
RUN npm run build

# 使用 Nginx 来服务构建后的静态文件
FROM nginx:alpine

# 将构建后的文件从前一个步骤复制到 Nginx 的默认静态文件目录
COPY --from=build /app/dist /usr/share/nginx/html

# 暴露端口
EXPOSE 80

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]