const express = require("express");
const bodyParser = require("body-parser");
const http = require("http");
const cors = require("cors");
const Config = require("./config");
const showRouter = require("./routers/show");

const app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use("/show", showRouter);

const port = Config.port;
const httpServer = http.createServer(app);
httpServer.listen(port, () => {
  console.log("%s is listening on %s", app.name, port, new Date());
});