class Shows:
    @staticmethod
    def get_shows_query():
        return f"select * from shows;"
    @staticmethod
    def post_show_query(body):        
        return f"INSERT INTO `shows` (`name`, `score`) VALUES({body.name}, {body.score});"    
    @staticmethod
    def update_show_query(body):
        return f"UPDATE `shows` SET `score` = '{body.score}' WHERE (`name` = '{body.name}');"    
    @staticmethod
    def delete_show_query(body):
        return f"DELETE FROM `showsdb`.`shows` WHERE (`name` = '{body.name}');"
