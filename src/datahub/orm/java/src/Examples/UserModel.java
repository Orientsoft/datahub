package Examples;

import DataHubAnnotations.Association;
import DataHubAnnotations.Association.LoadTypes;
import DataHubAnnotations.Column;
import DataHubAnnotations.NoDownload;
import DataHubAnnotations.Table;
import DataHubAnnotations.VarCharField;
import DataHubAnnotations.Verify;
import DataHubAnnotations.Association.AssociationTypes;
import DataHubORM.DataHubException;
import DataHubORM.DataHubModel;
import DataHubORM.QueryRefinementObject;

@Verify()
@Table(name="users")
public class UserModel extends DataHubModel<UserModel>{
	
	//require constructor with no arguments to set defaults
	public UserModel() throws DataHubException {
		super();
		// TODO Auto-generated constructor stub
	}

	@Column(name="username")
	@VarCharField(size=1000)
	public String username;
	
	@NoDownload
	@Column(name="password")
	@VarCharField(size=1000)
	public String password;
	
	@Association(associationType = AssociationTypes.HasAndBelongsToMany, linkingTable = "testuser", leftTableForeignKey = "test_id",rightTableForeignKey = "user_id", foreignKey = "user_id")
	public TestDatahubArrayList tests;
	
	
	@Override
	public synchronized boolean validate(){
		return true;
	}
	
	@Override
	public synchronized void beforeSave(){
		
	}
	
	@Override
	public synchronized void afterSave(){
		
	}
	
	@Override
	public synchronized void beforeDestroy(){
		
	}
	
	@Override
	public synchronized void afterDestroy(){
		
	}

	//override this method to set defaults for fields in class
	@Override
	public void setDefaults(){
		this.password = "lol";
	}
	
	//Override this method to use this default query refinment object in all queries for class
	//where query refinment object not specified
	@Override
	public QueryRefinementObject getDefaultQueryRefinemnetObject(){
		return new QueryRefinementObject();
	}
	
	
}