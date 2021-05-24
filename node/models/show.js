const sql = require("../dataAccess/db");

// constructor
const Show = function(show) {
  this.name = show.name;
  this.score = show.score;
};

Show.getAll = result => {
  sql.query("SELECT * FROM shows", (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    console.log("shows: ", res);
    result(null, res);
  });
};

Show.create = (newShow, result) => {
  sql.query("INSERT INTO shows SET ?", newShow, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(err, null);
      return;
    }

    console.log("created customer: ", { id: res.insertId, ...newCustomer });
    result(null, { id: res.insertId, ...newCustomer });
  });
};

Show.update = (name, show, result) => {
  sql.query(
    "UPDATE customers SET name = ?, score = ? WHERE name = ?",
    [show.name, show.score, name],
    (err, res) => {
      if (err) {
        console.log("error: ", err);
        result(null, err);
        return;
      }

      if (res.affectedRows == 0) {
        // not found Customer with the name
        result({ kind: "not_found" }, null);
        return;
      }

      console.log("updated customer: ", { id: id, ...customer });
      result(null, { id: id, ...customer });
    }
  );
};

Show.remove = (name, result) => {
  sql.query("DELETE FROM customers WHERE name = ?", name, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    if (res.affectedRows == 0) {
      // not found Customer with the name
      result({ kind: "not_found" }, null);
      return;
    }

    console.log("deleted customer with name: ", name);
    result(null, res);
  });
};

module.exports = Show;